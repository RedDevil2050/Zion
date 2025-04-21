def run(symbol: str) -> dict:
    upcoming_actions = [
        {"type": "Dividend", "value": 10, "date": "2024-05-15"},
        {"type": "Bonus", "ratio": "1:1", "date": "2024-06-01"},
    ]
    action_summary = ", ".join([f"{a['type']} on {a['date']}" for a in upcoming_actions])
    score = 85 if upcoming_actions else 50
    verdict = "ACTIVE CORPORATE EVENTS" if score >= 80 else "NO MAJOR EVENTS"
    return {
        "agent": "event/corporate_action_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"Upcoming Actions: {action_summary}"
    }
