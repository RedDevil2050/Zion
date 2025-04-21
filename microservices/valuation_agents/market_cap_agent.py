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
    mc = 1200000
    score = 90 if mc > 1000000 else 60
    verdict = "LARGE CAP" if score > 85 else "MID CAP"
    return {
        "agent": "valuation/market_cap_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"Market Cap: ₹{mc} Cr"
    }
