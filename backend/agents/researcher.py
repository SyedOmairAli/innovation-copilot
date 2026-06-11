from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-15-preview"
)

class ResearchAgent:

    def run(self, idea_summary: str):

        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[
                {"role": "system", "content": "You are a research assistant."},
                {"role": "user", "content": f"""
Expand research areas for this idea:

{idea_summary}

Include:
- Related technologies
- Existing solutions
- Data sources
- Risks
"""}
            ]
        )

        return response.choices[0].message.content