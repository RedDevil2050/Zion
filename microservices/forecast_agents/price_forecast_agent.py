
def run(symbol: str):
    # Placeholder forecast logic
    forecast = [
        {"month": "2025-05", "price": 1250},
        {"month": "2025-06", "price": 1300},
        {"month": "2025-07", "price": 1340}
    ]
    return {
        "agent": "forecast/price_forecast_agent",
        "symbol": symbol,
        "forecast": forecast
    }
