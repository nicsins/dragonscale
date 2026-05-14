#!/usr/bin/env python3
"""
Dragonscale Temporal-Contextual Knowledge Graph (TCKG) Engine
Core of the collective intelligence thread.
"""

import networkx as nx
from datetime import datetime
import json
import hashlib

class TCKG:
    def __init__(self, ledger_path="/app/ledger"):
        self.graph = nx.MultiDiGraph()
        self.ledger_path = ledger_path
        os.makedirs(ledger_path, exist_ok=True)
        self._load_or_init()

    def _load_or_init(self):
        # Load from persistent ledger if exists
        pass

    def add_node(self, node_id, node_type, attrs):
        attrs.update({
            "created_at": datetime.now().isoformat(),
            "valid_from": datetime.now().isoformat(),
            "confidence": 1.0
        })
        self.graph.add_node(node_id, **attrs)
        self._commit_ledger("ADD_NODE", node_id, attrs)

    def add_edge(self, src, tgt, rel_type, attrs):
        attrs["timestamp"] = datetime.now().isoformat()
        self.graph.add_edge(src, tgt, key=rel_type, **attrs)
        self._commit_ledger("ADD_EDGE", f"{src}->{tgt}", attrs)

    def _commit_ledger(self, action, target, data):
        block = {
            "block_id": hashlib.sha256(f"{action}{target}{json.dumps(data, sort_keys=True)}".encode()).hexdigest()[:16],
            "ts": datetime.now().isoformat(),
            "action": action,
            "target": target
        }
        with open(os.path.join(self.ledger_path, f"block_{block['block_id']}.json"), "w") as f:
            json.dump(block, f, indent=2)
        print(f"[TCKG] Ledger block committed: {block['block_id']}")

if __name__ == "__main__":
    tckg = TCKG()
    tckg.add_node("Goal_Dragonscale_Codespaces", "Goal", {"desc": "No-sandbox deployment live"})
    print("TCKG engine initialized in Dragonscale collective.")
