# Dragonscale Zero-Trust Container Model (Tailscale-Inspired)

**Version:** 1.2 - Zero-Trust Partitioned Nodes  
**Date:** May 14, 2026  
**Principle:** "Trust but verify — containers for all, full access only for verified trusted nodes."

## Core Design (Tailscale Analogy)
- Every Dragonscale node runs as a **containerized agent** (Docker) for consistent, portable sharing of knowledge and resources (Beowulf-style CPU/GPU pooling, ledger access).
- **Networking**: Headscale + Tailscale mesh for secure, zero-config P2P (exact same model as Tailscale nodes).
- **Knowledge/Resource Sharing**: All inter-node communication happens inside containers. Shared volumes are mounted read-only by default for collective learning.

## Zero-Trust for Foreign / Untrusted Nodes
- **Default State**: Every incoming connection from a non-whitelisted node is treated as **foreign**.
- **Partitioned Environment**:
  - Runs in strict sandbox (Docker --security-opt no-new-privileges, read-only filesystem, limited capabilities).
  - Encrypted partitioned profile access: Only anonymized aggregates + zero-knowledge queries to the ledger.
  - No direct file system access to host user data.
  - Resource sharing limited to inference cycles only (no persistent storage writes outside container).
- **Verification Flow**:
  1. Node presents cryptographic identity (Tailscale node key + Dragonscale ledger signature).
  2. If not in trusted list → auto-partitioned mode.
  3. Continuous monitoring + anomaly detection via collective sentiment thread.

## Trusted Nodes (Full Access, No Sandbox)
- **Whitelist**: User explicitly marks nodes as trusted (via wizard or config: "trusted_nodes": ["Fluffy-Kitty-Node-02", ...]).
- **Privileges**:
  - Full read/write access to authorized host folders for encrypted profile learning.
  - Unrestricted resource sharing (full Beowulf pooling).
  - Direct ledger append rights (higher weight in collective intelligence).
  - Can execute privileged tasks (e.g., local file operations, system commands with user approval).
- **Security**: Still runs in container for isolation from host OS, but with elevated capabilities and volume mounts.

## Implementation in Current Stack
- **docker-compose.yml**: Two profiles — `trusted` and `foreign` (different security_opt and volumes).
- **dragonscale_connector_wizard.py**: New prompt: "Is this node trusted by you? (yes/no)" → sets flag in config/node_config.json.
- **Bootstrap**: Reads flag and launches appropriate Docker profile or Python native mode for trusted nodes.
- **Ledger**: Records node trust level on every interaction for collective audit.

## Benefits
- Maximum security for foreign nodes (zero-trust by default).
- Maximum utility and speed for your own trusted devices (fluffy kitty, laptops, servers).
- Perfect Tailscale compatibility for easy mesh expansion.
- Aligns with Dragonscale goals: collective learning without compromising privacy or control.

**This model ensures the network scales safely while giving trusted nodes (like your personal devices) the power they deserve.**