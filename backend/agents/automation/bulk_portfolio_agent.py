
import csv

def run(file_path: str):
    symbols = []
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                symbol = row.get("Symbol") or row.get("symbol")
                if symbol:
                    symbols.append(symbol.strip().upper())
    except Exception as e:
        return {"agent": "bulk_portfolio_agent", "error": str(e)}

    return {
        "agent": "bulk_portfolio_agent",
        "symbols": symbols,
        "count": len(symbols),
        "status": "ready"
    }
