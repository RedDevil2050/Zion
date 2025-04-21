
def run(symbol: str):
    ev_ebitda = 12  # sample realistic value
    verdict = "BUY" if ev_ebitda < 10 else "HOLD" if ev_ebitda < 14 else "SELL"
    return {
        "agent": "valuation/ev_ebitda_agent",
        "symbol": symbol,
        "ev_ebitda": ev_ebitda,
        "verdict": verdict
    }
