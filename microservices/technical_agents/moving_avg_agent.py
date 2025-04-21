def run(symbol: str) -> dict:
    sma_50 = 102
    sma_200 = 95
    score = 80 if sma_50 > sma_200 else 60
    verdict = "GOLDEN CROSS" if sma_50 > sma_200 else "DEATH CROSS"
    return {
        "agent": "technical/moving_avg_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"SMA-50: {sma_50}, SMA-200: {sma_200}"
    }
