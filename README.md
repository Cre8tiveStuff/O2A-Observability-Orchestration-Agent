# O2A — Observability, Orchestration, Agent

**Open towards Team Collaborations & Contract Opportunities.**

A closed-loop AI system where agents verify their own output. O2A orchestrates a full pipeline into one system: a LangChain agent reasons about which tool to call — including multi-step sequences — every action is logged automatically with full chain correlation, and the same evaluation logic used on raw data gets reused to score the agent's own answers.

## How it works

- **evaluate_dataset** — checks data completeness and quality (from [AIG Data Quality Eval Engine](https://github.com/Cre8tiveStuff/AIG-Data-Quality-Eval-Platform))
- **answer_question** — retrieves and answers questions from procurement contracts, now with context curation applied via [CCL](https://github.com/Cre8tiveStuff/Context-Curation-Ledger) before the prompt is built (from [procurement-rag](https://github.com/Cre8tiveStuff/procurement-rag))
- **refresh_index_tool** — safely re-indexes a new contract file, protected against duplicate work by [ARC](https://github.com/Cre8tiveStuff/ARC-Agentic-Reasoning-Chain)'s `@idempotent` decorator
- A real LangChain agent, powered by locally-run `llama3.1:8b` via Ollama, decides which tool(s) to call and in what order — no hardcoded routing, verified with a real multi-step reasoning test
- Every tool call automatically logs its input, output, and verification status to SQLite, correlated by a shared `run_id` per reasoning chain

## Verified: real multi-tool reasoning

```bash
python3 test_full_chain.py
```

Gives the agent a single instruction requiring both `refresh_index_tool` and `answer_question` in sequence, then asserts the real model output called them in the correct order — not synthetic test data, genuine live reasoning, confirmed passing.

## Installation

```bash
git clone https://github.com/Cre8tiveStuff/O2A-Observability-Orchestration-Agent.git
cd O2A-Observability-Orchestration-Agent
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

Requires [Ollama](https://ollama.com) running locally with `llama3.1:8b` pulled.

## Usage

```bash
python3 agent.py
```

## Running tests

```bash
pytest tests/
```

## Part of a five-repo system

O2A is the orchestration layer tying together four sibling projects: [AIG Data Quality Eval Engine](https://github.com/Cre8tiveStuff/AIG-Data-Quality-Eval-Platform), [procurement-rag](https://github.com/Cre8tiveStuff/procurement-rag), [ARC](https://github.com/Cre8tiveStuff/ARC-Agentic-Reasoning-Chain), and [CCL](https://github.com/Cre8tiveStuff/Context-Curation-Ledger) — each independently built and tested, wired together here into one verified, working system.

## Tech stack

Python · LangChain · Ollama · SQLite · ChromaDB · Redis · tiktoken