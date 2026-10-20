"""Runs a user-supplied Python snippet in-process and returns stdout."""

from __future__ import annotations

import contextlib
import io
import traceback


def execute(source: str, timeout_note: str = "") -> str:
    """Exec is intentional: this agent is the local operator's tool, not a public sandbox."""
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(source, {"__name__": "__dragonscale_exec__"}, {})  # noqa: S102
    except Exception:
        return buf.getvalue() + traceback.format_exc()
    out = buf.getvalue().strip()
    if timeout_note:
        out = f"{out}\n{timeout_note}".strip()
    return out or "(no stdout)"
