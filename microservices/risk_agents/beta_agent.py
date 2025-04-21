def run(symbol: str) -> dict:
    beta = 1.2  # Simulated beta value
    score = 70 if 0.8 <= beta <= 1.3 else 50
    verdict = "MARKET-ALIGNED" if 0.8 <= beta <= 1.3 else "VOLATILE"
    return {
        "agent": "risk/beta_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"Beta: {beta}"
    }
