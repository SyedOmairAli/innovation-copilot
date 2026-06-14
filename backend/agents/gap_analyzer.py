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

class GapAnalyzer:

    def run(self, research_data: str):

        fabric = FabricIQ()
        semantic_model = fabric.get_semantic_context()

        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[
                {"role": "system", "content": "You find innovation gaps."},
                {"role": "user", "content": f"""
Analyze missing gaps and opportunities:

{research_data}

Use this semantic evaluation model:

- Innovation Weight: {semantic_model['innovation_weight']}
- Impact Weight: {semantic_model['impact_weight']}
- Feasibility Weight: {semantic_model['feasibility_weight']}

Find:

- Unsolved problems
- Weaknesses in current solutions
- Innovation opportunities
- Expected business impact
- Feasibility considerations

For each opportunity, explain:
1. Why it is a gap
2. How impactful it is
3. How feasible it is
4. Priority level (High / Medium / Low)
"""}
            ]
        )

        return response.choices[0].message.content