"""Writes a small, runnable Python snippet for a concrete coding task."""

from __future__ import annotations

from agents.llm import chat


SYSTEM = (
    "You are the Dragonscale coder. Return only a short Python solution. "
    "Prefer the standard library. No proprietary SDK imports."
)


def code(task: str) -> str:
    return chat(SYSTEM, task)
