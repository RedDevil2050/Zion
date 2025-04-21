import logging
import time

def log_execution(func):
    def wrapper(symbol):
        start = time.time()
        try:
            result = func(symbol)
            duration = round(time.time() - start, 2)
            logging.info(f"[{func.__name__}] Success | Symbol: {symbol} | Time: {duration}s")
            return result
        except Exception as e:
            logging.error(f"[{func.__name__}] Failure | Symbol: {symbol} | Error: {str(e)}")
            return {"agent": func.__name__, "verdict": "ERROR", "score": 0, "insight": str(e)}
    return wrapper


@log_execution
def run(symbol: str) -> dict:
    pcf = 10.2
    score = 80 if pcf < 12 else 60
    verdict = "REASONABLE" if score >= 75 else "EXPENSIVE"
    return {
        "agent": "valuation/price_to_cash_flow_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"P/CF Ratio: {pcf}"
    }
