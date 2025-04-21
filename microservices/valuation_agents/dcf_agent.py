
def run(symbol: str):
    # Simple DCF calculation with fixed projection
    eps = 40
    growth_rate = 0.08
    discount_rate = 0.12
    years = 5
    future_eps = eps
    npv = 0
    for i in range(1, years + 1):
        future_eps *= (1 + growth_rate)
        npv += future_eps / ((1 + discount_rate) ** i)
    verdict = "BUY" if npv > 1000 else "HOLD" if abs(npv - 1000) < 100 else "SELL"
    return {
        "agent": "valuation/dcf_agent",
        "symbol": symbol,
        "dcf_value": npv,
        "verdict": verdict
    }
