def run(symbol: str) -> dict:
    esg_score = 72.5  # Simulated ESG score out of 100
    score = 85 if esg_score >= 70 else 65 if esg_score >= 50 else 40
    verdict = "HIGH ESG COMPLIANCE" if score >= 80 else "MODERATE" if score >= 60 else "WEAK"
    return {
        "agent": "esg/esg_score_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"ESG Score: {esg_score}"
    }
