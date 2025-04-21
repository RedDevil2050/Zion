
def run(data):
    verified = True if data.get('price') and float(data['price']) > 0 else False
    return {"verified": verified, "reason": "Price validation successful" if verified else "Invalid price data"}
