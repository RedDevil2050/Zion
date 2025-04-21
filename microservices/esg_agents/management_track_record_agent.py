def run(symbol: str) -> dict:
    track_record = {
        "tenure": 8,  # in years
        "return_during_tenure": 3.5  # in multiple
    }
    score = 90 if track_record["return_during_tenure"] >= 3 else 70 if track_record["tenure"] >= 5 else 50
    verdict = "EXCELLENT MANAGEMENT" if score >= 85 else "STABLE" if score >= 70 else "UNPROVEN"
    return {
        "agent": "esg/management_track_record_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"Tenure: {track_record['tenure']} yrs, Return: {track_record['return_during_tenure']}x"
    }
