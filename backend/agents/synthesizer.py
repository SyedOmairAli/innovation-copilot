from openai import AzureOpenAI
import os
from dotenv import load_dotenv
from tools.iq_layer import FabricIQ

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-15-preview"
)

class Synthesizer:

    def run(self, plan, research, gaps):

        fabric = FabricIQ()
        semantic_model = fabric.get_semantic_context()

        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior AI product strategist."
                },
                {
                    "role": "user",
                    "content": f"""
Create a professional innovation intelligence report.

You are acting as a senior enterprise AI strategy system.

Use the following inputs:

PLAN:
{plan}

RESEARCH:
{research}

GAPS:
{gaps}

Semantic Scoring Model (Fabric IQ):
- Innovation Weight: {semantic_model['innovation_weight']}
- Impact Weight: {semantic_model['impact_weight']}
- Feasibility Weight: {semantic_model['feasibility_weight']}

Return STRICT FORMAT:

## Executive Summary
Provide a 3–5 line high-level summary.

## Problem Statement
Clearly define the core problem.

## Market Context
Explain the industry and opportunity space.

## Key Insights
Bullet points of most important findings.

## Identified Innovation Opportunities
List and explain opportunities.

## Proposed Solution
Describe the best solution direction.

## Innovation Scoring (0–10)
- Innovation Score:
- Impact Score:
- Feasibility Score:

Explain briefly how scores were derived using the semantic model.

## Reasoning Trace
Step-by-step explanation of how the system:
1. Interpreted the plan
2. Processed research
3. Identified gaps
4. Generated final recommendation

## Knowledge Sources Used
List any inferred or referenced knowledge areas.

## Final Verdict
One strong paragraph summarizing decision outcome and recommendation.
"""
                }
            ]
        )

        return response.choices[0].message.content