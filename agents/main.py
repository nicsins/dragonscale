from fastapi import FastAPI
from datetime import datetime
import os

app = FastAPI(title="Dragonscale Agents - Collective Intelligence")

@app.get("/")
def root():
    return {
        "message": "Dragonscale Network Active",
        "timestamp": datetime.now().isoformat(),
        "status": "Collective learning enabled. No-sandbox mode: " + os.getenv("DRAGONSCALE_NO_SANDBOX", "false"),
        "tckg": "Connected",
        "ledger": "Immutable blocks recording every intelligence update"
    }

@app.post("/ingest_instruction")
def ingest(instruction: str, user_id: str = "domiNic"):
    return {
        "status": "Instruction parsed and committed to TCKG",
        "action": "Planning CoA with temporal + causal awareness",
        "profile_update": f"Encrypted partition for {user_id} updated with new context"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
