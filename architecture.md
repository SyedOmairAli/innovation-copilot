flowchart TD

%% ========== USER ==========
User[User Input: Innovation Idea]

%% ========== ORCHESTRATION ==========
Orchestrator[Orchestrator\nMulti-Agent Controller]

User --> Orchestrator

%% ========== AGENTS ==========
Planner[Planner Agent\nWork IQ Context]
Research[Research Agent\nFoundry IQ Grounding]
Gap[Gap Analyzer\nFabric IQ Scoring]
Synth[Synthesizer\nExecutive Report Generator]

Orchestrator --> Planner
Planner --> Research
Research --> Gap
Gap --> Synth

%% ========== IQ LAYERS ==========
WorkIQ[(Work IQ\nWork Context Signals)]
FoundryIQ[(Foundry IQ\nKnowledge Grounding)]
FabricIQ[(Fabric IQ\nSemantic Scoring Model)]

Planner --> WorkIQ
Research --> FoundryIQ
Gap --> FabricIQ
Synth --> FabricIQ

%% ========== OUTPUT ==========
Output[Final Output\nInnovation Intelligence Report]

Synth --> Output

%% ========== FEEDBACK LOOP ==========
Output --> Orchestrator