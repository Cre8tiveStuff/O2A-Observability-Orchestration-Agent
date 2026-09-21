from agent import agent, start_new_run, _run_state
from chain_logger import get_chain
from test_helpers import assert_tool_order

start_new_run()

result = agent.invoke({
    "messages": [{
        "role": "user",
        "content": "First index the file /home/cre8tive257/procurement-rag/data/processed/contract_A_saas_license.txt, then tell me the delivery timeline agreed upon by Supplier Inc."
    }]
})

print(result)
print()

chain = get_chain(_run_state["run_id"])
print("Chain log:", chain)

assert_tool_order(result, ["refresh_index_tool", "answer_question"])
print("PASSED: agent called tools in correct order")
