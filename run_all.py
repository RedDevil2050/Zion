
import sys
from backend import orchestrator
import importlib.util
import os
import traceback
import sys
if len(sys.argv) == 1:
    sys.argv.append('RELIANCE')  # default test symbol

# --- Optional: Manually run stealth agents individually before orchestrator ---
def run_stealth_agents(symbol):
    print("\n🔍 Running Stealth Agents...\n")
    stealth_dir = os.path.join(os.path.dirname(__file__), "microservices", "stealth_scrapers")
    results = []

    for root, _, files in os.walk(stealth_dir):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                agent_path = os.path.join(root, file)
                try:
                    spec = importlib.util.spec_from_file_location("agent", agent_path)
                    agent = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(agent)

                    if hasattr(agent, "run"):
                        result = agent.run(symbol)
                        results.append({
                            "agent": file,
                            "status": "SUCCESS",
                            "output": result
                        })
                    else:
                        results.append({
                            "agent": file,
                            "status": "FAILED",
                            "output": "No run() method found"
                        })
                except Exception as e:
                    results.append({
                        "agent": file,
                        "status": "ERROR",
                        "output": str(e)
                    })
    return results

# --- Run full orchestrator pipeline ---
def run_full_pipeline(symbol):
    print("\n⚙️ Running Orchestrator Pipeline...\n")
    try:
        result = orchestrator.run(symbol)
        print("✅ Final Verdict:", result["final_verdict"])
        print("🔢 Final Score:", result["final_score"])
        print("🧠 Agents Used:", result["agents_used"])
        print("\n📋 Agent Results (Sample):")
        for r in result["agent_results"][:10]:
            print(f"- {r.get('agent', 'unknown')}: {r.get('verdict', '?')} | Score: {r.get('score', 0)}")
        return result
    except Exception as e:
        print("❌ Error running orchestrator:", str(e))
        traceback.print_exc()

# --- Main Entry Point ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❗Usage: python run_all.py <STOCK_SYMBOL>")
        sys.exit(1)

    symbol = sys.argv[1].upper()

    # Step 1: Run all stealth agents
    stealth_results = run_stealth_agents(symbol)
    for r in stealth_results:
        print(f"[{r['status']}] {r['agent']} → {str(r['output'])[:120]}...")

    # Step 2: Run the full orchestrator
    run_full_pipeline(symbol)
