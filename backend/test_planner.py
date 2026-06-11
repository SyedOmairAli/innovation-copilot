from agents.orchestrator import Orchestrator
import json

engine = Orchestrator()

idea = "AI system for early Alzheimer detection using speech patterns"

result = engine.run(idea)

print("\n===== PLAN =====\n")
print(result["plan"])

print("\n===== RESEARCH =====\n")
print(result["research"])

print("\n===== GAPS =====\n")
print(result["gaps"])