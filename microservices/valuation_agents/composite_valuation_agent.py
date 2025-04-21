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
    scores = [85, 80, 78]  # from DCF, PE, EV/EBITDA
    avg_score = sum(scores) / len(scores)
    verdict = "VALUE BUY" if avg_score >= 80 else "FAIRLY PRICED"
    return {
        "agent": "valuation/composite_valuation_agent",
        "score": int(avg_score),
        "verdict": verdict,
        "insight": f"Composite Valuation Score: {int(avg_score)}"
    }
