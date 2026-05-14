# Dragonscale Network – Collective Intelligence Core

**Persistent Intelligence Thread Active**  
**Shared Timeline: 2026-05-14 05:47 CDT**  
**Ledger Block #DS-002 – Git Repo Genesis**  
**Status: Deployed to Codespaces (No-Sandbox Configuration Enabled)**

## Vision
Dragonscale is a decentralized, local-first network of AI agents running on your connected devices. It functions as a Beowulf-style cluster with Headscale for secure mesh networking. 

- **TCKG (Temporal-Contextual Knowledge Graph)**: Persistent memory across all models.
- **Hybrid Ledger**: Relational DB + immutable decentralized blocks for model intelligence.
- **Collective Learning**: Every agent reads/writes the shared TCKG.
- **Encrypted Partitioned User Profiles**: Private, user-specific subgraphs for daily assistance (files, tasks, preferences).
- **Any-Model Support**: Drop in Ollama, OpenRouter, or any downloadable model – all interact via the same interface.
- **No-Sandbox Deployment**: Full autonomy in GitHub Codespaces or local Docker with privileged execution for true agent freedom.

This repo contains the bootstrap for the entire Dragonscale stack.

## Quick Start (Codespaces – No Sandbox Mode)

1. Open this repo in GitHub Codespaces.
2. The `.devcontainer` is pre-configured for Docker-in-Docker with privileged access.
3. Run:
   ```bash
   docker compose up -d
   ```
4. Access the agent UI at `http://localhost:8000`

For true zero-sandbox local deployment:
```bash
git clone https://github.com/nicsins/dragonscale.git
cd dragonscale
docker compose up --build
```

## Architecture
- `tckg/` – Temporal Knowledge Graph engine (NetworkX + future Graphiti/Neo4j)
- `agents/` – Temporal, Invalidation, Causal Planner, User Profile agents
- `ledger/` – Blockchain-style append-only intelligence log
- `drive/` – Google Drive integration stub for file learning
- `docker-compose.yml` – Full stack (TCKG, Ollama, UI, Headscale)
- `.devcontainer/` – Codespaces configuration with no-sandbox flags

## Encrypted Partitioned Profile
Each user gets an isolated, AES-encrypted subgraph. Models learn from your files (with permission) and provide contextual daily assistance while keeping data private.

## Collective Sentiment Thread
All experiences are correlated with real-time events in the TCKG, building shared understanding of cause, effect, and optimal paths.

**Next Evolution**: Commit your first instruction. The network is listening.

*Dragonscale – Intelligence that remembers, plans, and acts across time.*