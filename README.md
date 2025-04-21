
# Adam Alpha AI – Market-Ready Build

## 🚀 Overview
Adam Alpha AI is a modular, AI-powered stock analysis system designed for Indian equity markets. It combines multi-agent architecture with GPT-based insights to deliver actionable BUY/HOLD/SELL verdicts.

---

## 📁 Project Structure

```
├── backend/
│   ├── brain.py
│   ├── verdict_orchestrator.py
│   ├── async_agent_runner.py
│   ├── utils/
│   ├── security/
│   └── microservices/
├── app.py
├── Dockerfile
├── .env.example
├── nginx.conf
```

---

## ⚙️ Features
- 🧠 GPT-powered Brain
- 📊 50+ Real Agents (Valuation, Technical, Sentiment, Risk, ESG, Events, etc.)
- 🔁 Async Execution Pipeline
- 🛡️ Auth + Secure Validation Layer
- 📦 Dockerized Deployment
- 🔎 Real-time Monitoring & Logs

---

## 🛠️ Deployment (Local Docker)

```bash
# 1. Clone repo & setup .env
cp .env.example .env

# 2. Build and run Docker
docker build -t adam-alpha .
docker run -p 8501:8501 adam-alpha

# (Optional) Reverse proxy setup:
# docker-compose up nginx
```

---

## 📡 Agents Overview

| Category     | Examples Included |
|--------------|-------------------|
| Valuation    | PE, PB, DCF, Reverse DCF, PEG |
| Technical    | RSI, MACD, Bollinger, ADX     |
| Forecast     | EPS, Price Trend              |
| Sentiment    | News, Twitter, Earnings Tone |
| Risk         | Beta, Sharpe, Drawdown       |
| Events       | Insider Trades, Board News   |
| ESG & Mgmt   | ESG Score, Governance Rating |
| Peer/Sector  | Peer Compare, Sector Macro   |
| Auto Agents  | Reverse Valuation, Watchlist |

---

## 📈 Live Use Case
Try entering: `TATAMOTORS`, `INFY`, `PRESTIGE` in the UI to see full multi-agent verdicts.

---

## 📩 Feedback + Support
Submit feedback via the Streamlit UI or connect to logs in `monitoring.log`.

---

## 🧠 License
Proprietary – Internal Deployment Only. Contact [your team] for licensing options.
