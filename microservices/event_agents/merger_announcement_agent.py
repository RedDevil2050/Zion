def run(symbol: str) -> dict:
    merger_news = [
        {"target": "ABC Ltd", "type": "Acquisition", "status": "Pending"}
    ]
    score = 85 if merger_news else 55
    verdict = "MERGER/ACQUISITION IN PLAY" if merger_news else "NO ANNOUNCEMENT"
    summary = ", ".join([f"{m['type']} of {m['target']} ({m['status']})" for m in merger_news])
    return {
        "agent": "event/merger_announcement_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"Merger News: {summary}"
    }
