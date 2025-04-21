
def run(symbol: str):
    factors = {
        "value": 80,
        "momentum": 65,
        "growth": 70,
        "risk": 50
    }
    score = sum(factors.values()) / len(factors)
    verdict = "BUY" if score > 65 else "HOLD"
    return {
        "agent": "intelligence/factor_score_agent",
        "symbol": symbol,
        "factors": factors,
        "composite_score": score,
        "verdict": verdict
    }
