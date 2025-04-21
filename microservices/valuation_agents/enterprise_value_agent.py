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
    ev = 120000
    score = 85 if ev < 150000 else 60
    verdict = "REASONABLE EV" if score >= 80 else "ELEVATED EV"
    return {
        "agent": "valuation/enterprise_value_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"Enterprise Value: ₹{ev} Cr"
    }
