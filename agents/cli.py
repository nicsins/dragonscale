"""Immediate entrypoint.

Examples:
  python -m agents.cli "what should we log after a failed deploy"
  python -m agents.cli --self-test
"""

from __future__ import annotations

import argparse
import json
import sys

from agents.coordinator import Coordinator
from agents.ledger import Ledger
from agents.profile import Profile


def self_test() -> int:
    ledger = Ledger("data/selftest.db")
    event_id = ledger.add_event("selftest", "boot", "agents import", desired="verify chain")
    ledger.record_outcome(event_id, "ok", 1.0)
    profile = Profile("selftest", root="data/profiles")
    profile.remember("self-test note")
    ok = ledger.verify() and "self-test note" in profile.load()["notes"]
    print(json.dumps({"ok": ok, "event_id": event_id, "db": str(ledger.path)}))
    ledger.close()
    return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Dragonscale coordinator")
    parser.add_argument("task", nargs="?", help="Task for the coordinator")
    parser.add_argument("--user", default="local")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    if not args.task:
        parser.error("pass a task or --self-test")
    result = Coordinator(user_id=args.user).handle(args.task)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
