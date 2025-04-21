
from backend.orchestrator import run_agent, load_agents_from_dir
import concurrent.futures

def system_test(symbol):
    agents_paths = load_agents_from_dir("../backend/agents/valuation")  # you can expand categories as needed
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_agent, symbol, path) for path in agents_paths]
        results = [f.result() for f in futures]
    print(f"System-level test results for {symbol}:")
    for r in results:
        print(r)

if __name__ == "__main__":
    system_test("INFY")
