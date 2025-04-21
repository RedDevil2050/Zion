def run(symbol: str) -> dict:
    max_drawdown = -22.5  # Simulated max drawdown in percentage
    score = 80 if max_drawdown > -25 else 55
    verdict = "CONTROLLED RISK" if score >= 75 else "HIGH DRAWDOWN"
    return {
        "agent": "risk/drawdown_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"Max Drawdown: {max_drawdown}%"
    }
