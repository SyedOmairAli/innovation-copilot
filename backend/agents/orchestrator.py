from agents.planner import PlannerAgent
from agents.researcher import ResearchAgent
from agents.gap_analyzer import GapAnalyzer
from agents.synthesizer import Synthesizer

class Orchestrator:

    def __init__(self):
        self.planner = PlannerAgent()
        self.researcher = ResearchAgent()
        self.gap = GapAnalyzer()
        self.synth = Synthesizer()

    def run(self, idea: str):

        idea = idea.strip()

        print("\n[1] Running Planner...")
        plan = self.planner.run(idea)

        print("\n[2] Running Research...")
        research = self.researcher.run(plan)

        print("\n[3] Running Gap Analysis...")
        gaps = self.gap.run(research)

        print("\n[4] Running Synthesis...")
        final_report = self.synth.run(plan, research, gaps)

        return {
            "idea": idea,
            "plan": plan,
            "research": research,
            "gaps": gaps,
            "final_report": final_report
        }