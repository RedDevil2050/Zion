
import os
import hashlib
import json

CACHE_FILE = "brain_cache.json"

def cache_response(symbol, result):
    key = hashlib.sha256(symbol.encode()).hexdigest()
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            db = json.load(f)
    else:
        db = {}
    db[key] = result
    with open(CACHE_FILE, "w") as f:
        json.dump(db, f)

def get_cached_response(symbol):
    key = hashlib.sha256(symbol.encode()).hexdigest()
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            db = json.load(f)
        return db.get(key, None)
    return None

def analyze_outputs(agent_outputs):
    symbol = agent_outputs[0]['symbol'] if agent_outputs else 'UNKNOWN'
    cached = get_cached_response(symbol)
    if cached:
        return cached

    reasoning = "Based on AI logic, we recommend HOLD."  # Replace with real model call
    final = {
        "symbol": symbol,
        "verdict": "HOLD",
        "explanation": reasoning
    }

    cache_response(symbol, final)
    return final
