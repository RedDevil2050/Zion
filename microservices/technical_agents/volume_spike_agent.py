
def run(symbol: str):
    spike_pct = 35
    verdict = "BUY" if spike_pct > 30 else "HOLD"
    return {
        "agent": "technical/volume_spike_agent",
        "symbol": symbol,
        "volume_spike_pct": spike_pct,
        "verdict": verdict
    }
