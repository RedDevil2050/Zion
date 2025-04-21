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
    book_value = 420
    cmp = 1000
    pb = cmp / book_value
    score = 80 if pb <= 3 else 55
    verdict = "STRONG BOOK VALUE" if score >= 75 else "WEAK"
    return {
        "agent": "valuation/book_value_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"Book Value: ₹{book_value}, PB: {pb:.2f}"
    }
