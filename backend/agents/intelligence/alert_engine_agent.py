
def run(symbol: str, agent_outputs: list):
    triggers = []
    for agent in agent_outputs:
        if "rsi" in agent["agent"] and agent.get("verdict") == "BUY":
            triggers.append("RSI Triggered (Oversold)")
        if "insider_trade" in agent["agent"]:
            if "BUY" in agent.get("verdict", ""):
                triggers.append("Insider Buy Detected")
        if "growth_valuation" in agent["agent"] and agent.get("verdict") == "BUY":
            triggers.append("High Growth Signal")

    return {
        "agent": "alert_engine_agent",
        "symbol": symbol,
        "alerts": triggers,
        "status": "ALERT" if triggers else "STABLE"
    }
