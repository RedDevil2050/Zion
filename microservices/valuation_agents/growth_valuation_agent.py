
def run(symbol: str):
    eps_growth = 0.2  # assumed
    roe = 0.18
    peg = 1.2
    verdict = "BUY" if peg < 1 else "HOLD" if peg < 2 else "SELL"
    return {
        "agent": "valuation/growth_valuation_agent",
        "symbol": symbol,
        "growth_rate": eps_growth,
        "roe": roe,
        "peg": peg,
        "verdict": verdict
    }
