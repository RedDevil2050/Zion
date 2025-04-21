
def run(symbol: str):
    peers = [
        {"symbol": "PEER1", "pe": 22, "eps": 38},
        {"symbol": "PEER2", "pe": 26, "eps": 41},
    ]
    avg_pe = sum(p['pe'] for p in peers) / len(peers)
    verdict = "UNDERVALUED" if avg_pe > 25 else "FAIRLY VALUED"
    return {
        "agent": "intelligence/peer_compare_agent",
        "symbol": symbol,
        "peers": peers,
        "avg_pe": avg_pe,
        "verdict": verdict
    }
