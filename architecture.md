```mermaid

flowchart TD

%% ========== USER ==========
User[User Input: Innovation Idea]

%% ========== ORCHESTRATION ==========
Orchestrator[Orchestrator Multi-Agent Controller]

User --> Orchestrator

%% ========== AGENTS ==========
Planner[Planner Agent Work IQ Context]
Research[Research Agent Foundry IQ Grounding]
Gap[Gap Analyzer Fabric IQ Scoring]
Synth[Synthesizer Executive Report Generator]

Orchestrator --> Planner
Planner --> Research
Research --> Gap
Gap --> Synth

%% ========== IQ LAYERS ==========
WorkIQ[(Work IQ Work Context Signals)]
FoundryIQ[(Foundry IQ Knowledge Grounding)]
FabricIQ[(Fabric IQ Semantic Scoring Model)]

Planner --> WorkIQ
Research --> FoundryIQ
Gap --> FabricIQ
Synth --> FabricIQ

%% ========== OUTPUT ==========
Output[Final Output Innovation Intelligence Report]

Synth --> Output

%% ========== FEEDBACK LOOP ==========
Output --> Orchestrator