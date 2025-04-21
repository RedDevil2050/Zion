
def run(symbol: str):
    # Realistic PB logic
    data = {'pb': 3.2, 'book_value': 273.98, 'price': 1000}
    fair_value = data['book_value'] * data['pb']
    deviation = (data['price'] - fair_value) / fair_value * 100
    verdict = "BUY" if deviation < -20 else "HOLD" if -20 <= deviation <= 20 else "SELL"
    return {
        "agent": "valuation/pb_ratio_agent",
        "symbol": symbol,
        "pb": data['pb'],
        "book_value": data['book_value'],
        "fair_value": fair_value,
        "price": data['price'],
        "deviation": deviation,
        "verdict": verdict
    }
