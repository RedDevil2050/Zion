
def run(symbol: str):
    ps_ratio = 3.5
    verdict = "BUY" if ps_ratio < 2 else "HOLD" if ps_ratio < 5 else "SELL"
    return {
        "agent": "valuation/price_to_sales_agent",
        "symbol": symbol,
        "ps_ratio": ps_ratio,
        "verdict": verdict
    }
