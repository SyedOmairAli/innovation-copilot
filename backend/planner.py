import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-12-01-preview"
)

class PlannerAgent:

    def run(self, idea: str):

        messages = [
            {
                "role": "system",
                "content": "You are an innovation research planner."
            },
            {
                "role": "user",
                "content": f"""
Analyze this invention idea:

{idea}

Return:
1. Research domains
2. Search keywords
3. Patent search keywords
4. Innovation directions
"""
            }
        ]

        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=messages,
            temperature=0.7
        )

        return response.choices[0].message.content