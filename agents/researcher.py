"""Looks up context the coordinator already has. Does not invent sources."""

from __future__ import annotations

from agents.llm import chat


SYSTEM = (
    "You are the Dragonscale researcher. Answer from the notes given. "
    "If the notes are not enough, say what is missing. Do not invent citations."
)


def research(task: str, notes: list[str]) -> str:
    context = "\n".join(f"- {n}" for n in notes) or "(no prior notes)"
    return chat(SYSTEM, f"Task:\n{task}\n\nKnown notes:\n{context}")
