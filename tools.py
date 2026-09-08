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
