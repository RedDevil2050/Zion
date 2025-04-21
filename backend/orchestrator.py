import os
import importlib.util
import concurrent.futures
import re

# Weights for composite scoring
CATEGORY_WEIGHTS = {
    "valuation": 0.4,
    "sentiment": 0.2,
    "technical": 0.2,
    "risk": 0.2,
}


def clean_number(val):
    """Convert strings like '₹123.45' to float 123.45, else return numeric or None."""
    if isinstance(val, (int, float)):
        return float(val)
    if isinstance(val, str):
        num = re.sub(r"[^\d\.]", "", val)
        try:
            return float(num)
        except ValueError:
            return None
    return None


def load_agents_from_dir(dir_path):
    """List all .py agent files in a directory."""
    paths = []
    for f in os.listdir(dir_path):
        if f.endswith(".py") and not f.startswith("__"):
            paths.append(os.path.join(dir_path, f))
    return paths


def run_agent(symbol, path):
    """Dynamically import and run an agent, tagging its category."""
    try:
        spec = importlib.util.spec_from_file_location("agent", path)
        agent = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(agent)
        if hasattr(agent, "run"):
            result = agent.run(symbol)
            category = os.path.basename(os.path.dirname(path))
            result["category"] = category
            return result
    except Exception as e:
        return {"agent": os.path.basename(path), "symbol": symbol, "error": str(e), "category": None}


def compute_valuation(stealth_results):
    """Compute MoS-based valuation verdict and score."""
    data = {"price": None, "eps": None, "pe": None}
    for r in stealth_results:
        if data["price"] is None and "price" in r:
            data["price"] = clean_number(r["price"])
        if data["eps"] is None and "eps" in r:
            data["eps"] = clean_number(r["eps"])
        if data["pe"] is None and "pe" in r:
            data["pe"] = clean_number(r["pe"])
    if all(data.values()):
        est = data["eps"] * data["pe"]
        mos = (est - data["price"]) / data["price"]
        if mos > 0.25:
            return {"category": "valuation", "verdict": "BUY", "score": 90, "insight": f"Strong margin of safety (~{mos*100:.1f}%)"}
        if mos > 0.10:
            return {"category": "valuation", "verdict": "HOLD", "score": 65, "insight": f"Moderate margin of safety (~{mos*100:.1f}%)"}
        return {"category": "valuation", "verdict": "SELL", "score": 40, "insight": f"No margin of safety (~{mos*100:.1f}%)"}
    return {"category": "valuation", "verdict": "SELL", "score": 0, "insight": "Insufficient data"}


def compute_composite_score(results):
    """Combine category scores into a weighted composite score and verdict."""
    cat_scores = {cat: [] for cat in CATEGORY_WEIGHTS}
    val_score = None
    for r in results:
        cat = r.get("category")
        score = r.get("score")
        if cat == "valuation":
            val_score = score
        if cat in cat_scores and isinstance(score, (int, float)):
            cat_scores[cat].append(score)
    composite = 0.0
    for cat, weight in CATEGORY_WEIGHTS.items():
        if cat == "valuation" and val_score is not None:
            composite += val_score * weight
        elif cat_scores[cat]:
            composite += (sum(cat_scores[cat]) / len(cat_scores[cat])) * weight
    composite = max(0, min(100, composite))
    if composite > 70:
        final_verdict = "BUY"
    elif composite > 50:
        final_verdict = "HOLD"
    else:
        final_verdict = "SELL"
    return {"verdict": final_verdict, "score": composite}


def run(symbol, live_mode=True):
    base_dir = os.path.dirname(__file__)
    agent_dir = os.path.join(base_dir, "agents")
    root_dir = os.path.dirname(os.path.dirname(__file__))
    stealth_dir = os.path.join(root_dir, "microservices", "stealth_scrapers")

    # 1. Stealth phase
    stealth_paths = load_agents_from_dir(stealth_dir)
    with concurrent.futures.ThreadPoolExecutor() as ex:
        stealth_results = list(ex.map(lambda p: run_agent(symbol, p), stealth_paths))

    # 2. Valuation from stealth
    valuation_result = compute_valuation(stealth_results)
    all_results = stealth_results + [valuation_result]

    # 3. Analysis phase (optional)
    analysis_results = []
    if live_mode:
        for category in ["sentiment", "technical", "risk"]:
            dir_path = os.path.join(agent_dir, category)
            paths = load_agents_from_dir(dir_path)
            with concurrent.futures.ThreadPoolExecutor() as ex:
                analysis_results += list(ex.map(lambda p: run_agent(symbol, p), paths))
        all_results += analysis_results

    # 4. Composite scoring
    if live_mode:
        comp = compute_composite_score(all_results)
        final_verdict, final_score = comp["verdict"], comp["score"]
    else:
        final_verdict, final_score = valuation_result["verdict"], valuation_result["score"]

    return {
        "symbol": symbol,
        "final_verdict": final_verdict,
        "final_score": final_score,
        "agents_used": len(stealth_results) + len(analysis_results) + 1,
        "agent_results": all_results + [{
            "agent": "live_intelligence",
            "verdict": final_verdict,
            "score": final_score,
            "insight": f"Composite {'live' if live_mode else 'valuation-only'} intelligence"
        }]
    }

if __name__ == "__main__":
    # Simple test harness
    test_symbols = ["RELIANCE", "TCS", "INFY"]
    for sym in test_symbols:
        result = run(sym, live_mode=True)
        print(f"\n=== {sym} → Verdict: {result['final_verdict']} @ {result['final_score']:.1f} ===")
        for res in result["agent_results"]:
            print(res)
