from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-15-preview"
)

class Synthesizer:

    def run(self, plan, research, gaps):

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
Create a professional innovation report.

PLAN:
{plan}

RESEARCH:
{research}

GAPS:
{gaps}

Return STRICT format:

## Problem Summary
...

## Market Context
...

## Key Insights
...

## Proposed Solution
...

## Innovation Scores
- Innovation: X/10
- Feasibility: X/10
- Impact: X/10

## Final Verdict
1 paragraph summary
"""
                }
            ]
        )

        return response.choices[0].message.content