
def run(symbol: str):
    yield_pct = 1.2
    verdict = "BUY" if yield_pct > 2 else "HOLD" if yield_pct > 1 else "SELL"
    return {
        "agent": "valuation/dividend_yield_agent",
        "symbol": symbol,
        "dividend_yield": yield_pct,
        "verdict": verdict
    }
