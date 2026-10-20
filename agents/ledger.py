"""Single-instance hash-chained ledger. Relational tables, one sqlite file."""

from __future__ import annotations

import hashlib
import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


class Ledger:
    def __init__(self, path: str | None = None):
        raw = path or os.getenv("LEDGER_PATH", "data/dragonscale.db")
        self.path = Path(raw).expanduser()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        self._schema()

    def _schema(self) -> None:
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_id TEXT UNIQUE NOT NULL,
                ts TEXT NOT NULL,
                agent TEXT NOT NULL,
                kind TEXT NOT NULL,
                description TEXT NOT NULL,
                desired TEXT,
                prev_hash TEXT NOT NULL,
                hash TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS outcomes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_id TEXT NOT NULL,
                ts TEXT NOT NULL,
                actual TEXT NOT NULL,
                success REAL DEFAULT 0,
                FOREIGN KEY (event_id) REFERENCES events(event_id)
            );
            CREATE TABLE IF NOT EXISTS implications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_id TEXT NOT NULL,
                text TEXT NOT NULL,
                weight REAL DEFAULT 0.5,
                unexpected INTEGER DEFAULT 0,
                FOREIGN KEY (event_id) REFERENCES events(event_id)
            );
            """
        )
        self.conn.commit()

    def _last_hash(self) -> str:
        row = self.conn.execute(
            "SELECT hash FROM events ORDER BY id DESC LIMIT 1"
        ).fetchone()
        return row["hash"] if row else "GENESIS"

    def add_event(
        self,
        agent: str,
        kind: str,
        description: str,
        desired: str = "",
        implications: list[str] | None = None,
        unexpected: bool = False,
    ) -> str:
        ts = _now()
        event_id = f"evt_{ts.replace(':', '').replace('-', '').replace('+', '')[:20]}_{agent[:8]}"
        prev = self._last_hash()
        payload = json.dumps(
            {
                "event_id": event_id,
                "ts": ts,
                "agent": agent,
                "kind": kind,
                "description": description,
                "desired": desired,
                "prev": prev,
            },
            sort_keys=True,
        )
        digest = hashlib.sha256(payload.encode()).hexdigest()
        self.conn.execute(
            """
            INSERT INTO events (event_id, ts, agent, kind, description, desired, prev_hash, hash)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (event_id, ts, agent, kind, description, desired, prev, digest),
        )
        for text in implications or []:
            self.conn.execute(
                "INSERT INTO implications (event_id, text, unexpected) VALUES (?, ?, ?)",
                (event_id, text, 1 if unexpected else 0),
            )
        self.conn.commit()
        return event_id

    def record_outcome(self, event_id: str, actual: str, success: float = 0.0) -> None:
        self.conn.execute(
            "INSERT INTO outcomes (event_id, ts, actual, success) VALUES (?, ?, ?, ?)",
            (event_id, _now(), actual, success),
        )
        self.conn.commit()

    def recent(self, limit: int = 10) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            "SELECT event_id, ts, agent, kind, description FROM events ORDER BY id DESC LIMIT ?",
            (limit,),
        ).fetchall()
        return [dict(row) for row in rows]

    def verify(self) -> bool:
        rows = self.conn.execute(
            "SELECT event_id, ts, agent, kind, description, desired, prev_hash, hash FROM events ORDER BY id"
        ).fetchall()
        prev = "GENESIS"
        for row in rows:
            if row["prev_hash"] != prev:
                return False
            payload = json.dumps(
                {
                    "event_id": row["event_id"],
                    "ts": row["ts"],
                    "agent": row["agent"],
                    "kind": row["kind"],
                    "description": row["description"],
                    "desired": row["desired"] or "",
                    "prev": row["prev_hash"],
                },
                sort_keys=True,
            )
            if hashlib.sha256(payload.encode()).hexdigest() != row["hash"]:
                return False
            prev = row["hash"]
        return True

    def close(self) -> None:
        self.conn.close()
