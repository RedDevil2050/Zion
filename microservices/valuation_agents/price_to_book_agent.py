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
    pb_ratio = 2.8
    score = 80 if pb_ratio < 3 else 60
    verdict = "REASONABLE" if score >= 75 else "OVERVALUED"
    return {
        "agent": "valuation/price_to_book_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"Price to Book Ratio: {pb_ratio}"
    }
