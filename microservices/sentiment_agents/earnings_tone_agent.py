
def run(symbol: str):
    # Simulate parsing of transcript tone
    tone_score = 0.4  # positive tone
    tone = "positive" if tone_score > 0.2 else "neutral" if tone_score > -0.2 else "negative"
    return {
        "agent": "sentiment/earnings_tone_agent",
        "symbol": symbol,
        "tone": tone,
        "score": tone_score
    }
