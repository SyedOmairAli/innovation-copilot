```mermaid

sequenceDiagram

participant U as User
participant O as Orchestrator
participant P as Planner
participant R as Research
participant G as Gap Analyzer
participant S as Synthesizer

U->>O: Submit Innovation Idea
O->>P: Decompose Idea
P->>R: Send research domains + keywords
R->>G: Send expanded research context
G->>S: Send gaps + opportunity scoring
S->>O: Final Innovation Report
O->>U: Structured Intelligence Output