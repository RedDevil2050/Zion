
def best_of_n(av_results):
    verified_results = [r for r in av_results if r['verified']]
    return {"overall_verified": len(verified_results) > len(av_results)/2, "verified_results": verified_results}
