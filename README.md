# O2A -- Observability, Orchestration, Agent

**Open towards Team Collaborations & Contract Opportunities**

A closed loop AI system where agents verify their own output.  O2A orchestrates two projects (a data quality evaluator and a local RAG assistant) into one system:  
a langChain agent reasons about which tool to call. Every action is logged automatically, and the same evaluation logic used on raw data gets reused to score the agent's own answer.

## How it works

-**evaluate_dataset** - checks data completeness and quality (frrom AIG Data Quality Eval Engine)
-**answer_question** - retrieves and answer questions from procurement contracts (from procurement-rag)
- An actual Langchain agent, powered by locally-run 'llama3.1:8b' via ollama, decides which tool to call based on the question - no hardcoded routing.
-Every tool call automatically logs its input, output, and verification status to SQLite.

## Installation

```bash
git clone https://github.com/Cre8tiveStuff/O2A-Observability-Orchestration-Agent.git
cd O2A-Observability-Orchestration-Agent
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

Requires [Ollama](https://ollama.com) running locally with 'llama3.1:8b' pulled.

## Usage

```bash
python3 agent.py
```

## Running tests

```bash
pytest tests/
```

## Tech stack

Python - LangChain - Ollama - SQLite - ChromaDB
