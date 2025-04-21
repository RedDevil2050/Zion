
def run(symbol: str):
    adx = 28
    verdict = "BUY" if adx > 25 else "HOLD"
    return {
        "agent": "technical/adx_agent",
        "symbol": symbol,
        "adx": adx,
        "verdict": verdict
    }
