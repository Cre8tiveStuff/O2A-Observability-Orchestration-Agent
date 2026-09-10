from    db import init_db, log_action

from    src.evaluators import DataQualityEvaluator

def     evaluate_dataset(records):
        evaluator = DataQualityEvaluator(records)
        result = evaluator.run_all()
        status = result["metrics"][0]["status"]
        score = result["metrics"][0]["score_pct"]
        log_action("evaluate_dataset", records, result, status, score)
        return result

if   __name__ == "__main__":
        init_db()
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
            result = {"answer": "No relevant context found.", "chunks": []}
            log_action("answer_question", question, result, "FAIL", 0)
            return result
        prompt = format_rag_prompt(question, chunks)
        answer = generate_answer(prompt, model_name=model_name)
        result = {"answer": answer, "chunks":  chunks}
        log_action("answer_question", question, result, "PASS", len(chunks))
        return result
