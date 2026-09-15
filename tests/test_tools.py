from    tools import evaluate_dataset
from    db import init_db

init_db()


def     test_evaluate_dataset_returns_expected_shape():
        result = evaluate_dataset([{"prompt":  "Hi", "response":  "A real answer here."}])
        assert "summary" in result
        assert "metrics" in result
        assert result["summary"]["total_records"] == 1

def     test_evaluate_dataset_flags_missing_data():
        result = evaluate_dataset([{"prompt":  "Hi", "response":  None}])
        completeness = result["metrics"][0]
        assert completeness["null_count"] == 1
