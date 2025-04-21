def run(symbol: str) -> dict:
    recent_trades = [
        {"type": "Buy", "quantity": 10000, "price": 1500},
        {"type": "Sell", "quantity": 5000, "price": 1450},
    ]
    net_qty = sum([t["quantity"] if t["type"] == "Buy" else -t["quantity"] for t in recent_trades])
    score = 85 if net_qty > 0 else 60 if net_qty == 0 else 40
    verdict = "POSITIVE SIGNAL" if net_qty > 0 else "NEUTRAL" if net_qty == 0 else "NEGATIVE SIGNAL"
    return {
        "agent": "event/insider_trade_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"Net Insider Activity: {net_qty} shares"
    }
