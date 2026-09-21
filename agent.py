from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_core.tools import Tool
from tools import evaluate_dataset, answer_question, refresh_index_tool
from chain_logger import new_run_id, log_step, get_chain

llm = ChatOllama(model="llama3.1:8b")

_run_state = {"run_id": None, "step": 0}


def start_new_run():
    _run_state["run_id"] = new_run_id()
    _run_state["step"] = 0


def _logged(tool_name, func):
    def wrapper(text):
        _run_state["step"] += 1
        log_step(_run_state["run_id"], _run_state["step"], tool_name)
        return func(text)
    return wrapper


def eval_wrapper(text):
    return str(evaluate_dataset([{"response": text}]))


def rag_wrapper(text):
    return str(answer_question(text, db_dir="/home/cre8tive257/procurement-rag/data/chroma_db"))


def refresh_wrapper(text):
    return str(refresh_index_tool(text))


tools = [
    Tool(name="evaluate_dataset", func=_logged("evaluate_dataset", eval_wrapper), description="Checks data quality and completeness of a piece of text."),
    Tool(name="answer_question", func=_logged("answer_question", rag_wrapper), description="Answers questions about procurement contracts."),
    Tool(name="refresh_index_tool", func=_logged("refresh_index_tool", refresh_wrapper), description="Indexes a new contract file into the vector store. Provide the file path as input."),
]

agent = create_agent(model=llm, tools=tools)

if __name__ == "__main__":
    start_new_run()
    result = agent.invoke({"messages": [{"role": "user", "content": "what is the delivery timeline agreed upon by Supplier Inc?"}]})
    print(result)
    print("Chain log:", get_chain(_run_state["run_id"]))