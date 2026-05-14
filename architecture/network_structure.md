# Dragonscale Network Structure

## 1. Dragonscale Network
- Local deployment on connected user devices (Bloomington, MN network).
- Headscale + Tailscale overlay for secure peer-to-peer mesh.
- Beowulf-style resource sharing: CPU/GPU pooling, load balancing across nodes.
- Always-available model iteration: Ollama primary, OpenRouter fallback, auto-switch on failure.

## 2. Blockchain-Like Ledger
- **Relational Layer**: PostgreSQL for structured data (events, actors, outcomes, user profiles).
- **Decentralized Block Layer**: IPFS + append-only logs for immutable intelligence records.
- **Hashing**: Every model contribution produces a block hash (e.g., 0xDRGN...).
- **Anonymization**: Transparency ensures private data remains encrypted and partitioned.

## 3. Data Access & Collective Learning
- All models query the ledger via zero-knowledge mechanisms.
- Encrypted partitioned profiles: Models learn user files, preferences, daily tasks.
- Persistent Intelligence Thread: Rolling context window (30-day history + 7-day projection).

## 4. Agent Architecture
- Instruction Parsing → Task Graph → Execution (Python venv + Docker sandbox).
- Feedback via Chat UI with sentiment analysis feeding collective thread.
- Full autonomy in Docker instances for helper agents.

## 5. Software Infrastructure
- Python + Venv for core logic.
- Docker + UI dashboard for monitoring nodes, ledger, model health.
- Bootstrap script: dragonscale_bootstrap.py (see /code/)

## Integration Notes from Conversations
- All proposals committed to ledger.
- Temporal fabric added in later iterations.
- User files interaction enabled with explicit permission gates.