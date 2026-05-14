#!/usr/bin/env python3
"""
Dragonscale Admin Console
Tailscale-inspired self-hosted UI for the collective intelligence network.
Features: Node status, Ledger viewer, Temporal Graph, Trust management, Collective Sentiment, Profile health.
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import json
from datetime import datetime
import os

app = FastAPI(title="Dragonscale Admin Console", version="1.2")

# Templates
templates = Jinja2Templates(directory="templates")

# Simulated live data (in real: query PostgreSQL + temporal graph + ledger)
def get_live_status():
    return {
        "network": "Dragonscale Mesh v1.2 (Zero-Trust Container Model)",
        "total_nodes": 1,
        "active_nodes": 1,
        "trusted_nodes": ["Bloomington-Sandbox-Node-01"],
        "foreign_nodes": 0,
        "ledger_blocks": 5,
        "temporal_fabric_status": "ACTIVE - 2 nodes in graph",
        "collective_sentiment": "Highly Positive (92% alignment)",
        "last_update": datetime.now().isoformat()
    }

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    status = get_live_status()
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "status": status,
        "nodes": [
            {
                "id": "Bloomington-Sandbox-Node-01",
                "location": "Bloomington, MN",
                "status": "LIVE - Trusted",
                "last_seen": "just now",
                "resources": "CPU: 4 cores, GPU: available",
                "trust_level": "FULL ACCESS"
            }
        ]
    })

@app.get("/ledger", response_class=HTMLResponse)
async def ledger_view(request: Request):
    return templates.TemplateResponse("ledger.html", {
        "request": request,
        "blocks": [
            {"hash": "0xDRGN594bf2c32baf", "type": "Temporal Fabric Init", "node": "Bloomington-Sandbox-Node-01", "time": "2026-05-14 09:54"},
            {"hash": "0xDRGNa1fe323d2c5924", "type": "Zero-Trust v1.2 Commit", "node": "System", "time": "2026-05-14 09:58"},
        ]
    })

@app.get("/graph", response_class=HTMLResponse)
async def temporal_graph(request: Request):
    return templates.TemplateResponse("graph.html", {
        "request": request,
        "message": "Temporal Graph: current_state_2026-05-14 → desired_outcome_vector (weight 0.87)"
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)