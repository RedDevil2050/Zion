
def run(symbol: str):
    pattern = "Hammer"
    bullish_patterns = ["Hammer", "Bullish Engulfing"]
    verdict = "BUY" if pattern in bullish_patterns else "HOLD"
    return {
        "agent": "technical/candlestick_pattern_agent",
        "symbol": symbol,
        "pattern": pattern,
        "verdict": verdict
    }
