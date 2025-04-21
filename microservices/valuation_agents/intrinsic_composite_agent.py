
def run(symbol: str):
    components = {
        "pe_verdict": "BUY",
        "pb_verdict": "HOLD",
        "dcf_verdict": "BUY",
        "growth_verdict": "HOLD"
    }
    votes = list(components.values())
    final = max(set(votes), key=votes.count)
    return {
        "agent": "valuation/intrinsic_composite_agent",
        "symbol": symbol,
        "components": components,
        "composite_verdict": final
    }
