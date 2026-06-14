from openai import AzureOpenAI
import os
from dotenv import load_dotenv
from tools.iq_layer import FoundryIQ

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-15-preview"
)

class ResearchAgent:

    def run(self, idea_summary: str):

        iq = FoundryIQ()
        knowledge = iq.retrieve_knowledge(idea_summary)

        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[
                {"role": "system", "content": "You are a research assistant."},
                {"role": "user", "content": f"""
Expand research areas for this idea:

{idea_summary}

Use the following grounded knowledge sources:

{knowledge['sources']}

Include:
- Related technologies
- Existing solutions
- Data sources
- Risks
- Market trends
- Research opportunities

Make sure to align findings with the provided knowledge sources.
"""}
            ]
        )

        return response.choices[0].message.content