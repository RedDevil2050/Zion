
from backend.brain import analyze_outputs

def generate_verdict(symbol, agent_outputs):
    try:
        # Analyze using AI brain
        brain_output = analyze_outputs(agent_outputs)
        return {
            "symbol": symbol,
            "verdict": "BUY" if "buy" in brain_output.lower() else "HOLD" if "hold" in brain_output.lower() else "SELL",
            "explanation": brain_output,
            "raw_data": agent_outputs
        }
    except Exception as e:
        return {
            "symbol": symbol,
            "verdict": "UNKNOWN",
            "error": str(e),
            "raw_data": agent_outputs
        }
