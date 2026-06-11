from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-02-15-preview"
)

class GapAnalyzer:

    def run(self, research_data: str):

        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[
                {"role": "system", "content": "You find innovation gaps."},
                {"role": "user", "content": f"""
Analyze missing gaps and opportunities:

{research_data}

Find:
- Unsolved problems
- Weaknesses in current solutions
- Innovation opportunities
"""}
            ]
        )

        return response.choices[0].message.content