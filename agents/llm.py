"""Chat against a local Ollama model, or OpenRouter if OPENROUTER_API_KEY is set."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request


class LLMError(RuntimeError):
    pass


def chat(system: str, user: str, model: str | None = None, timeout: int = 180) -> str:
    or_key = os.getenv("OPENROUTER_API_KEY", "").strip()
    force_ollama = os.getenv("FORCE_OLLAMA", "").lower() in {"1", "true", "yes"}
    if or_key and not force_ollama:
        return _openrouter(system, user, or_key, timeout)
    return _ollama(system, user, model, timeout)


def _ollama(system: str, user: str, model: str | None, timeout: int) -> str:
    host = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434").rstrip("/")
    chosen = model or os.getenv("DRAGONSCALE_MODEL", "qwen2.5:7b")
    body = json.dumps(
        {
            "model": chosen,
            "stream": False,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        }
    ).encode()
    req = urllib.request.Request(
        f"{host}/api/chat",
        data=body,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.URLError as exc:
        raise LLMError(
            f"Ollama unreachable at {host}. Start it and pull {chosen}. ({exc})"
        ) from exc
    message = data.get("message") or {}
    text = message.get("content") or ""
    if not text:
        raise LLMError(f"Empty Ollama response for model {chosen}")
    return text


def _openrouter(system: str, user: str, key: str, timeout: int) -> str:
    chosen = os.getenv("OPENROUTER_MODEL", "qwen/qwen-2.5-7b-instruct")
    body = json.dumps(
        {
            "model": chosen,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        }
    ).encode()
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=body,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode())
    except urllib.error.URLError as exc:
        raise LLMError(f"OpenRouter request failed: {exc}") from exc
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as exc:
        raise LLMError(f"Unexpected OpenRouter payload: {data}") from exc
