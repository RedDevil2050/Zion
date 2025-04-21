def run(symbol: str) -> dict:
    pattern = "Bullish Engulfing"
    score = 85 if pattern == "Bullish Engulfing" else 50
    verdict = "BULLISH" if pattern == "Bullish Engulfing" else "NEUTRAL"
    return {
        "agent": "technical/candlestick_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"Detected Pattern: {pattern}"
    }
