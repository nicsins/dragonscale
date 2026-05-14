# Dragonscale Deployment Context

**Repository:** https://github.com/nicsins/dragonscale  
**Version:** 1.1 - Live Deployment Ready  
**Date:** May 14, 2026  
**Owner:** domiNic (NSins7202)  
**Ledger Anchor:** 0xDRGN9c8d7e6f5a4b3c2d1e0f9a8b7c6d5e4f3a2b1c0d9e8f7a6b5c4d3e2f1a0

## What is Dragonscale?
A decentralized, local-first collective intelligence network of AI agents.  
- Runs on your devices (laptops, servers, edge devices).  
- Shares compute like a Beowulf cluster via Headscale mesh.  
- Maintains a hybrid ledger (PostgreSQL + decentralized blocks) for collective learning.  
- Every model develops temporal/contextual awareness, persistent intelligence threads, and encrypted partitioned profiles of the user.  
- Goal: Correlate collective actions with real-world outcomes for better decision-making and daily assistance.

## Architecture Summary (Reviewed & Approved)
- **Network**: Headscale + Tailscale for secure mesh; resource pooling.  
- **Ledger**: Relational DB (events, actors, outcomes) + IPFS-style immutable blocks.  
- **Temporal Fabric**: Graph + vector store for time-aware reasoning (actions → actors → path impacts → desired outcomes).  
- **Agents**: Python + Docker; auto model iteration (Ollama primary, OpenRouter fallback).  
- **User Profiles**: Encrypted partitions; models learn from authorized files/folders for personalized help.  
- **Wizard Connector**: Interactive setup for new nodes (this repo's new feature).

## Prerequisites for Live Deployment
- Python 3.10+  
- Docker & Docker Compose  
- PostgreSQL (local or managed)  
- Ollama (for local models) or OpenRouter API key  
- Headscale server or self-hosted control plane (or join existing mesh)  
- Tailscale client  
- (Optional) Neo4j for full temporal graph, pgvector extension  
- GitHub PAT or SSH for pushing updates (if contributing)

## Security & Privacy Notes
- All private data stays in encrypted partitions on your devices.  
- Zero-knowledge queries to collective ledger.  
- No data leaves your network unless you explicitly allow external model calls.  
- Wizard prompts only for necessary keys; never stores plaintext secrets in repo.

## Current State (All Files Reviewed)
- Core architecture, methodology, bootstrap, and temporal fabric validated.  
- Missing piece from prior: Implication Engine & closed-loop reality feedback → prioritized for v1.2.  
- This context + instructions + wizard connector complete the live deployment package.

**Ready for real-world nodes across user networks.**