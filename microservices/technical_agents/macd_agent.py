
def run(symbol: str):
    macd = 1.2
    signal = 1.0
    verdict = "BUY" if macd > signal else "SELL" if macd < signal else "HOLD"
    return {
        "agent": "technical/macd_agent",
        "symbol": symbol,
        "macd": macd,
        "signal": signal,
        "verdict": verdict
    }
