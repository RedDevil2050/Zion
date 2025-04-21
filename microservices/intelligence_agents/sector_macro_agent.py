
def run(symbol: str):
    macro_outlook = "positive"
    sector_growth = 0.12
    verdict = "BUY" if macro_outlook == "positive" and sector_growth > 0.08 else "HOLD"
    return {
        "agent": "intelligence/sector_macro_agent",
        "symbol": symbol,
        "macro_outlook": macro_outlook,
        "sector_growth": sector_growth,
        "verdict": verdict
    }
