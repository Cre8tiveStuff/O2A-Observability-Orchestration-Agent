from    tools import evaluate_dataset, answer_question

def     run(goal, records=None, question=None, db_dir=None):
            if records is not None:
                print(f"Routing to evaluate_dataset for goal:  {goal}")
                return evaluate_dataset(records)
            elif question is not None:
                print(f"Routing to answer_question for goal:  {goal}")
                return answer_question(question, db_dir=db_dir)

            else:
                return {"error":  "No matching tool for this goal."}

if      __name__ == "__main__":
            result = run(
                goal="Check if this data is complete",
                records=[{"prompt":  "Test", "response": "A real answer here."}]
            )
            print(result)
