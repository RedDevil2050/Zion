
import os
import json
import hashlib
from functools import lru_cache

CACHE_DIR = "cache"

def ensure_cache_dir():
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)

def hash_key(symbol, agent):
    return hashlib.sha256(f"{symbol}-{agent}".encode()).hexdigest()

@lru_cache(maxsize=128)
def memory_cache(symbol: str, agent: str, output: dict):
    return output

def disk_cache(symbol: str, agent: str, output: dict = None):
    ensure_cache_dir()
    key = hash_key(symbol, agent)
    path = os.path.join(CACHE_DIR, f"{key}.json")
    if output is not None:
        with open(path, "w") as f:
            json.dump(output, f)
    elif os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return None
