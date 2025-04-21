def run(symbol: str) -> dict:
    upcoming_meetings = [
        {"agenda": "Results Approval", "date": "2024-05-20"},
        {"agenda": "Fund Raising", "date": "2024-06-10"}
    ]
    agenda_summary = ", ".join([f"{m['agenda']} on {m['date']}" for m in upcoming_meetings])
    score = 80 if upcoming_meetings else 50
    verdict = "KEY BOARD MEETINGS" if score >= 75 else "NO SIGNIFICANT MEETINGS"
    return {
        "agent": "event/board_meeting_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"Upcoming Meetings: {agenda_summary}"
    }
