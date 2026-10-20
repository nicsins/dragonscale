"""Encrypted per-user partition. Facts stay local; only hashes go on the ledger."""

from __future__ import annotations

import json
import os
from pathlib import Path

from cryptography.fernet import Fernet


class Profile:
    def __init__(self, user_id: str = "local", root: str | None = None):
        base = Path(root or os.getenv("PROFILE_DIR", "data/profiles")).expanduser()
        base.mkdir(parents=True, exist_ok=True)
        self.user_id = user_id
        self.path = base / f"{user_id}.bin"
        self.key_path = base / ".profile.key"
        self._fernet = Fernet(self._key())

    def _key(self) -> bytes:
        env = os.getenv("DRAGONSCALE_PROFILE_KEY", "").strip()
        if env:
            return env.encode()
        if self.key_path.exists():
            return self.key_path.read_bytes().strip()
        key = Fernet.generate_key()
        self.key_path.write_bytes(key)
        self.key_path.chmod(0o600)
        return key

    def load(self) -> dict:
        if not self.path.exists():
            return {
                "user_id": self.user_id,
                "style": "direct",
                "notes": [],
                "tasks": [],
            }
        raw = self._fernet.decrypt(self.path.read_bytes())
        return json.loads(raw.decode())

    def save(self, data: dict) -> None:
        blob = self._fernet.encrypt(json.dumps(data).encode())
        self.path.write_bytes(blob)
        self.path.chmod(0o600)

    def remember(self, note: str) -> dict:
        data = self.load()
        notes = data.setdefault("notes", [])
        notes.append(note)
        data["notes"] = notes[-50:]
        self.save(data)
        return data
