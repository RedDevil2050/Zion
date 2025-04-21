from textblob import TextBlob

def run(symbol: str) -> dict:
    # Placeholder: replace with actual tweet fetch
    tweet = "The stock is doing great. Amazing momentum!"
    sentiment_score = TextBlob(tweet).sentiment.polarity
    score = int((sentiment_score + 1) * 50)
    verdict = "BULLISH" if score >= 65 else "NEUTRAL" if score >= 45 else "BEARISH"
    return {
        "agent": "sentiment/twitter_sentiment_agent",
        "score": score,
        "verdict": verdict,
        "insight": f"TextBlob Sentiment Score: {sentiment_score} from tweet: {tweet[:40]}..."
    }
