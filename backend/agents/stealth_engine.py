
import random
from backend.utils.logging_utils import log_event

AGENT_POOL = [
    "microservices/stealth_scrapers/moneycontrol_agent",
    "microservices/stealth_scrapers/stockedge_agent",
    "microservices/stealth_scrapers/trendlyne_agent",
    "microservices/stealth_scrapers/tickertape_agent"
]

def smart_fetch(symbol):
    selected = random.choice(AGENT_POOL)
    try:
        module_path = selected.replace("/", ".")
        agent = __import__(f"backend.agents.{module_path}", fromlist=["run"])
        result = agent.run(symbol)
        log_event("stealth_fetch", f"{selected} success", {"symbol": symbol})
        return result
    except Exception as e:
        log_event("stealth_fetch", f"{selected} failed", {"error": str(e)})
        return {"agent": selected, "symbol": symbol, "error": str(e)}
