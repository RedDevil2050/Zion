
def run(symbol: str):
    price = 950
    supertrend = 960
    verdict = "BUY" if price > supertrend else "SELL"
    return {
        "agent": "technical/supertrend_agent",
        "symbol": symbol,
        "price": price,
        "supertrend": supertrend,
        "verdict": verdict
    }
