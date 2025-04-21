
def run(symbol: str):
    # Realistic PE valuation logic
    data = {'pe': 25, 'eps': 40, 'price': 1000}  # would be fetched dynamically
    fair_value = data['eps'] * data['pe']
    margin_of_safety = (fair_value - data['price']) / fair_value * 100
    verdict = "BUY" if margin_of_safety > 20 else "HOLD" if 0 < margin_of_safety <= 20 else "SELL"
    return {
        "agent": "valuation/pe_ratio_agent",
        "symbol": symbol,
        "pe": data['pe'],
        "eps": data['eps'],
        "fair_value": fair_value,
        "margin_of_safety": margin_of_safety,
        "verdict": verdict
    }
