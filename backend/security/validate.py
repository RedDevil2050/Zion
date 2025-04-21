
import re

def validate_symbol(symbol: str) -> bool:
    return bool(re.fullmatch(r"[A-Z0-9]{1,10}", symbol.strip()))

def sanitize_input(data):
    return str(data).replace(";", "").replace("--", "")
