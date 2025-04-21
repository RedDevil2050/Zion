
from backend.utils.logging_utils import log_event

def run(symbol: str, agent_outputs: list):
    if not agent_outputs:
        return {"agent": "ask_adam_agent", "symbol": symbol, "message": "No data to summarize."}

    try:
        categories = {}
        for agent in agent_outputs:
            key = agent['agent'].split("/")[0]
            categories.setdefault(key, []).append(agent.get("verdict", "N/A"))

        summary = []
        for cat, verdicts in categories.items():
            vote = max(set(verdicts), key=verdicts.count)
            summary.append(f"{cat.upper()}: {vote} ({verdicts.count(vote)} votes)")

        final = " | ".join(summary)
        response = {
            "agent": "ask_adam_agent",
            "symbol": symbol,
            "smart_summary": final,
            "recommendation": "BUY" if final.count("BUY") > final.count("SELL") else "HOLD"
        }
        log_event("ask_adam_agent", "summary success", {"symbol": symbol})
        return response
    except Exception as e:
        log_event("ask_adam_agent", "summary fail", {"error": str(e)})
        return {"agent": "ask_adam_agent", "symbol": symbol, "error": str(e)}
