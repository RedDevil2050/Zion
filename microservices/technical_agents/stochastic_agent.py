
def run(symbol: str):
    k = 65
    d = 60
    verdict = "BUY" if k > d else "SELL" if k < d else "HOLD"
    return {
        "agent": "technical/stochastic_agent",
        "symbol": symbol,
        "stochastic_k": k,
        "stochastic_d": d,
        "verdict": verdict
    }
