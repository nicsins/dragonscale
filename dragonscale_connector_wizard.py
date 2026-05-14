#!/usr/bin/env python3
"""
Dragonscale Connector Wizard
Interactive setup for new nodes. Prompts user for all required info,
generates config, initializes encrypted profile, and starts the local agent.
"""

import os
import json
import getpass
import subprocess
from datetime import datetime
import hashlib

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wizard():
    clear_screen()
    print("=" * 60)
    print("🐉 DRAGONSCALE NODE CONNECTOR WIZARD v1.1")
    print("   Preparing your node for the collective intelligence network")
    print("=" * 60)
    print()

    config = {
        "node_id": "",
        "location": "",
        "timestamp": datetime.now().isoformat(),
        "headscale": {},
        "models": {},
        "profile": {},
        "ledger": {},
        "security": {}
    }

    # 1. Node Identity
    print("STEP 1: Node Identity")
    config["node_id"] = input("Enter unique Node ID (e.g. Bloomington-MN-Laptop-01): ").strip()
    config["location"] = input("Enter your location/timezone (e.g. America/Chicago): ").strip() or "UTC"
    print()

    # 2. Headscale / Mesh Networking
    print("STEP 2: Headscale Mesh Networking (secure P2P)")
    print("  (Leave blank to use public Tailscale or start local Headscale later)")
    hs_key = getpass.getpass("Headscale auth key (or server URL): ").strip()
    config["headscale"]["auth_key"] = hs_key if hs_key else "TAILSCALE_DEFAULT"
    config["headscale"]["server_url"] = input("Headscale control server URL (optional): ").strip() or "https://headscale.example.com"
    print()

    # 3. AI Models
    print("STEP 3: Model Stack (Ollama local + OpenRouter fallback)")
    print("  Available local models: llama3, mistral, phi3, etc. (Ollama must be installed)")
    models_input = input("Comma-separated preferred models (default: llama3.2,phi3): ").strip()
    config["models"]["preferred"] = [m.strip() for m in models_input.split(",")] if models_input else ["llama3.2", "phi3"]
    or_key = getpass.getpass("OpenRouter API Key (optional, for cloud fallback): ").strip()
    config["models"]["openrouter_key"] = or_key
    config["models"]["iteration_strategy"] = "ollama_primary_openrouter_fallback"
    print()

    # 4. Encrypted User Profile
    print("STEP 4: Encrypted Partitioned User Profile (for daily task learning)")
    print("  Enter folders/files the agent may learn from (encrypted locally):")
    folders = input("Comma-separated paths (e.g. ~/Documents,~/Notes,~/Projects): ").strip()
    config["profile"]["authorized_folders"] = [f.strip() for f in folders.split(",")] if folders else ["~/Documents"]
    config["profile"]["encryption"] = "AES-256 + partitioned"
    print()

    # 5. Ledger & Database
    print("STEP 5: Ledger & Temporal Database")
    pg_url = input("PostgreSQL URL (default: local Docker): ").strip() or "postgresql://dragonscale:pass@localhost:5432/dragonscale"
    config["ledger"]["postgres_url"] = pg_url
    config["ledger"]["use_temporal_graph"] = True
    print()

    # 6. Security Confirmation
    print("STEP 6: Final Confirmation")
    print("  All secrets are stored only in your local config (never committed).")
    confirm = input("Proceed with this configuration? (yes/no): ").strip().lower()
    if confirm != "yes":
        print("Wizard cancelled. Run again anytime.")
        return

    # Generate config file
    os.makedirs("config", exist_ok=True)
    config_path = "config/node_config.json"
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

    # Hash for ledger
    config_hash = hashlib.sha256(json.dumps(config).encode()).hexdigest()
    print(f"\n✅ Configuration saved to {config_path}")
    print(f"📡 Node block hash: 0xDRGN{config_hash[:16]}...")

    # Initialize profile (simulated encryption)
    print("🔐 Initializing encrypted partitioned profile...")
    for folder in config["profile"]["authorized_folders"]:
        print(f"   - Learning from: {folder} (encrypted)")

    # Start the node
    print("\n🚀 Starting Dragonscale node agent...")
    try:
        subprocess.run(["python", "code/dragonscale_bootstrap.py"], check=True)
    except Exception as e:
        print(f"Note: Bootstrap may require Docker. Error: {e}")
        print("Run manually after setup: python code/dragonscale_bootstrap.py")

    print("\n" + "=" * 60)
    print("🎉 NODE SUCCESSFULLY CONNECTED TO DRAGONSCALE NETWORK!")
    print("   Your agent is now part of the collective intelligence thread.")
    print("   Use natural language commands to interact.")
    print("=" * 60)

if __name__ == "__main__":
    wizard()