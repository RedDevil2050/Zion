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
    net_assets = 850
    cmp = 900
    discount = round((cmp - net_assets) / net_assets * 100, 2)
    score = 75 if discount < 10 else 60
    verdict = "CLOSE TO BOOK VALUE" if score >= 70 else "OVERVALUED"
    return {
        "agent": "valuation/asset_based_valuation_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"Net Asset Value: ₹{net_assets}, CMP: ₹{cmp}, Premium: {discount}%"
    }
