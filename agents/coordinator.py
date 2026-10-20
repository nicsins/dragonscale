"""Picks a specialist, records the event, stores a private note."""

from __future__ import annotations

from agents.coder import code
from agents.executor import execute
from agents.ledger import Ledger
from agents.profile import Profile
from agents.researcher import research


class Coordinator:
    def __init__(self, user_id: str = "local", agent_name: str = "coordinator"):
        self.user_id = user_id
        self.agent_name = agent_name
        self.ledger = Ledger()
        self.profile = Profile(user_id)

    def handle(self, task: str) -> dict:
        kind = _route(task)
        notes = self.profile.load().get("notes", [])
        if kind == "code":
            result = code(task)
        elif kind == "exec":
            source = task.split(":", 1)[1].strip()
            result = execute(source)
        else:
            result = research(task, notes)
        event_id = self.ledger.add_event(
            agent=self.agent_name,
            kind=kind,
            description=task[:500],
            desired=f"complete via {kind}",
            implications=[f"routed to {kind}"],
        )
        self.ledger.record_outcome(event_id, result[:1000], success=1.0)
        self.profile.remember(f"{kind}: {task[:180]}")
        return {
            "event_id": event_id,
            "route": kind,
            "result": result,
            "ledger_ok": self.ledger.verify(),
        }


def _route(task: str) -> str:
    low = task.lower()
    if low.startswith("exec:") or low.startswith("run:"):
        return "exec"
    if any(word in low for word in ("code", "function", "python", "script", "bug")):
        return "code"
    return "research"
