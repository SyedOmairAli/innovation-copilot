```md id="a1"
# System Architecture

```mermaid
flowchart TD

User[User Idea Input] --> Planner[Planner Agent]
Planner --> Research[Research Agent]
Research --> Gap[Gap Analyzer Agent]
Gap --> Synth[Synthesizer Agent]

Planner --> IQ1[Work IQ Layer]
Research --> IQ2[Foundry IQ Layer]
Gap --> IQ3[Fabric IQ Layer]

Synth --> Output[Final Innovation Report]