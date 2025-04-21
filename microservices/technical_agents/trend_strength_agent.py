
def run(symbol: str):
    trend_strength = 0.75
    verdict = "BUY" if trend_strength > 0.7 else "HOLD"
    return {
        "agent": "technical/trend_strength_agent",
        "symbol": symbol,
        "trend_strength": trend_strength,
        "verdict": verdict
    }
