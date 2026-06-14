import os
from dotenv import load_dotenv
from openai import AzureOpenAI
from tools.iq_layer import WorkIQ

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version="2024-12-01-preview"
)

class PlannerAgent:

    def run(self, idea: str):

        work_context = WorkIQ().get_context()

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

Organizational Context:
- Meeting Hours: {work_context['meeting_hours']}
- Focus Hours: {work_context['focus_hours']}
- Preferred Work Window: {work_context['preferred_work_window']}

Return:

1. Research domains
2. Search keywords
3. Patent search keywords
4. Innovation directions
5. Recommended focus areas considering the work context
"""
}
        ]

        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=messages,
            temperature=0.7
        )

        return response.choices[0].message.content