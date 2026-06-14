```mermaid

flowchart LR

WorkIQ[Work IQ]
FoundryIQ[Foundry IQ]
FabricIQ[Fabric IQ]

Planner[Planner Agent]
Research[Research Agent]
Gap[Gap Analyzer]
Synth[Synthesizer]

WorkIQ --> Planner
FoundryIQ --> Research
FabricIQ --> Gap
FabricIQ --> Synth

Planner --> Research --> Gap --> Synth