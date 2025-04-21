
import streamlit as st
import json
from backend.verdict_orchestrator import generate_verdict

st.set_page_config(page_title="Adam Alpha AI", layout="wide")

st.title("📊 Adam Alpha AI – Stock Verdict Engine")
symbol = st.text_input("Enter Stock Symbol (e.g., INFY, TATAMOTORS, PRESTIGE)", value="PRESTIGE")

if st.button("Run Analysis"):
    with st.spinner("Collecting data from agents..."):
        dummy_outputs = [
            {"agent": "valuation/pe_ratio_agent", "symbol": symbol, "pe": 25},
            {"agent": "forecast/price_forecast_agent", "symbol": symbol, "forecast": [{"month": "2025-05", "price": 1300}]},
            {"agent": "sentiment/news_sentiment_agent", "symbol": symbol, "sentiment": "positive", "score": 0.6},
        ]
        result = generate_verdict(symbol, dummy_outputs)
        st.subheader(f"🧠 Verdict: {result['verdict']}")
        st.markdown("### Reasoning")
        st.write(result['explanation'])

        with st.expander("Show Raw Agent Data"):
            st.json(result['raw_data'])

        st.markdown("### 💬 Feedback")
        feedback = st.radio("Was this verdict useful?", ("Yes", "No", "Not sure"))
        comments = st.text_area("Any comments or suggestions?")
        if st.button("Submit Feedback"):
            with open("feedback_log.txt", "a") as f:
                f.write(json.dumps({"symbol": symbol, "verdict": result["verdict"], "feedback": feedback, "comments": comments}) + "\n")
            st.success("Thank you for your feedback!")
