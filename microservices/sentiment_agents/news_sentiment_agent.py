
from textblob import TextBlob

def run(symbol: str):
    news_sample = "Prestige Estates posted strong results and plans to raise capital for expansion."
    sentiment_score = TextBlob(news_sample).sentiment.polarity
    sentiment = "positive" if sentiment_score > 0 else "negative" if sentiment_score < 0 else "neutral"
    return {
        "agent": "sentiment/news_sentiment_agent",
        "symbol": symbol,
        "sentiment": sentiment,
        "score": sentiment_score
    }
