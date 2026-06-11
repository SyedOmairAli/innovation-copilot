from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.orchestrator import Orchestrator

app = FastAPI(title="Innovation Copilot Multi-Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # 👈 IMPORTANT (not "*")
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = Orchestrator()

class IdeaRequest(BaseModel):
    idea: str

@app.post("/analyze")
def analyze(req: IdeaRequest):
    result = engine.run(req.idea)

    return {
        "input": req.idea,
        "pipeline": {
            "plan": result["plan"],
            "research": result["research"],
            "gaps": result["gaps"]
        },
        "final_report": result["final_report"]
    }