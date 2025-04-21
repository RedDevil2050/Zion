
def run(symbol: str):
    # Placeholder forecast logic
    eps_forecast = {
        "FY25": 15.2,
        "FY26": 18.4,
        "FY27": 21.1
    }
    return {
        "agent": "forecast/earnings_forecast_agent",
        "symbol": symbol,
        "eps_forecast": eps_forecast
    }
