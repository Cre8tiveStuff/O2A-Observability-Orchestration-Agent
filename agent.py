from    langchain_ollama import ChatOllama
from    langchain.agents import create_agent
from    langchain_core.tools import Tool
from    tools import evaluate_dataset, answer_question

llm =   ChatOllama(model="llama3.1:8b")

def     eval_wrapper(text):
        return str(evaluate_dataset([{"response":  text}]))

def     rag_wrapper(text):
        return str(answer_question(text, db_dir="/home/cre8tive257/procurement-rag/data/chroma_db"))

tools = [
        Tool(name="evaluate_dataset", func=eval_wrapper, description="Checks data quality and completeness of a piece of text."),
        Tool(name="answer_question", func=rag_wrapper, description="Answers questions about procurement contracts."),
  ]

agent = create_agent(model=llm, tools=tools)

if      __name__ == "__main__":
        result = agent.invoke({"messages":  [{"role": "user", "content":  "what is the delivery timeline agreed upon by Supplier Inc?"}]})
        print(result)
