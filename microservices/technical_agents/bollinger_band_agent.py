
def run(symbol: str):
    price = 980
    upper = 1020
    lower = 920
    verdict = "SELL" if price > upper else "BUY" if price < lower else "HOLD"
    return {
        "agent": "technical/bollinger_band_agent",
        "symbol": symbol,
        "price": price,
        "upper_band": upper,
        "lower_band": lower,
        "verdict": verdict
    }
