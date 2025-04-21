
def run(symbol: str):
    score = 82  # composite signal strength
    verdict = "ADD TO WATCHLIST" if score > 75 else "IGNORE"
    return {
        "agent": "automation/auto_watchlist_agent",
        "symbol": symbol,
        "score": score,
        "verdict": verdict
    }
