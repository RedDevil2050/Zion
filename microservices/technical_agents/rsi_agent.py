
def run(symbol: str):
    rsi = 62  # Simulated value
    verdict = "SELL" if rsi > 70 else "BUY" if rsi < 30 else "HOLD"
    return {
        "agent": "technical/rsi_agent",
        "symbol": symbol,
        "rsi": rsi,
        "verdict": verdict
    }
