from    src.evaluators import DataQualityEvaluator

def     evaluate_dataset(records):
        evaluator = DataQualityEvaluator(records)
        return evaluator.run_all()

if   __name__ == "__main__":
        sample = [
           {"prompt":  "Test", "response":  "This is a substantive answer."},
           {"prompt":  "Missing", "response":  None},

 ]
        print(evaluate_dataset(sample))

from    src.query_rag import query_vector_store, format_rag_prompt
from    src.generate_answer import generate_answer
from    pathlib import Path

def     answer_question(question, db_dir, top_k=2, model_name="llama3.2"):
        chunks = query_vector_store(query_text=question, db_dir=db_dir, top_k=top_k)
        if not chunks:
            return {"answer": "No relevant context found.", "chunks": []}
        prompt = format_rag_prompt(question, chunks)
        answer = generate_answer(prompt, model_name=model_name)
        return {"answer": answer, "chunks":  chunks}
