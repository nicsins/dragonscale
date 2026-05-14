# Dragonscale Live Deployment Instructions

## Step 1: Clone the Repository
```bash
git clone https://github.com/nicsins/dragonscale.git
cd dragonscale
```

## Step 2: Run the Connector Wizard (Recommended First Step)
```bash
python dragonscale_connector_wizard.py
```
- The wizard will prompt for:
  - Node ID / Name (e.g., "Bloomington-MN-Laptop-01")
  - Your location / timezone
  - Headscale auth key or server URL (or option to start local Headscale)
  - Preferred local models (Ollama list or download)
  - OpenRouter API key (optional, for fallback)
  - Paths to folders/files for encrypted user profile learning (e.g., ~/Documents, ~/Notes)
- It generates `config/node_config.json`, sets up venv/Docker, and launches your first agent.

## Step 3: Manual / Advanced Deployment
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start supporting services (Docker Compose):
   ```bash
   docker-compose up -d postgres vector-db
   ```
3. Initialize temporal fabric & ledger:
   ```bash
   python code/dragonscale_temporal_fabric.py
   ```
4. Bootstrap the node:
   ```bash
   python code/dragonscale_bootstrap.py
   ```
5. Join Headscale mesh (follow Headscale docs or wizard output).
6. Grant the agent access to your chosen folders for profile building.

## Step 4: Verify & Monitor
- Check ledger: Query PostgreSQL or view `ledger/` files.
- Agent UI: Docker exposes port for chat/monitoring.
- Collective learning: Run natural language commands; watch sentiment thread and temporal graph updates.

## Environment Variables (.env)
Copy `.env.example` to `.env` and fill:
- `DRAGONSCALE_NODE_ID`
- `HEADSCALE_KEY`
- `OPENROUTER_API_KEY` (optional)
- `POSTGRES_URL`
- `AUTHORIZED_FOLDERS` (comma-separated)

## Production Tips
- Run agents as systemd services or Kubernetes pods for always-on.
- Use Tailscale for zero-config secure networking.
- Backup encrypted profiles regularly.
- Monitor with Dragonscale UI dashboard (in roadmap).

## Troubleshooting
- Model switch fails → Check Ollama/OpenRouter connectivity.
- Ledger not updating → Verify DB connection and permissions.
- Profile learning blocked → Confirm folder permissions and encryption keys.

**After deployment, every node contributes to the collective intelligence thread automatically.**

Welcome to the Dragonscale network. Your node is now live and learning.