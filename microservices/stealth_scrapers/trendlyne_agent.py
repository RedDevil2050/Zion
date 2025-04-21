import logging
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(name)s %(message)s')

# Create a session with retry strategy
session = requests.Session()
retry_strategy = Retry(
    total=3,
    status_forcelist=[403, 429, 500, 502, 503, 504],
    allowed_methods=["HEAD", "GET", "OPTIONS"],
    backoff_factor=1
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)
session.mount("http://", adapter)

import requests

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def make_session():
    session = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=False
    )
    session.mount('https://', HTTPAdapter(max_retries=retries))
    session.headers.update({'User-Agent': 'Mozilla/5.0'})
    return session

_session = make_session()

from bs4 import BeautifulSoup
import time
import random

def run(symbol: str) -> dict:
    url = f"https://trendlyne.com/equity/{symbol.lower()}/"
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    ]
    headers = {
        "User-Agent": random.choice(user_agents)
    }

    try:
        time.sleep(random.uniform(1.5, 3.0))
        response = _session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        def safe_find(label):
            try:
                tag = soup.find("span", text=label)
                if tag:
                    return tag.find_next("span").text.strip()
            except Exception:
                return None

        pe_ratio = safe_find("PE TTM")
        eps = safe_find("EPS")
        roe = safe_find("ROE")
        market_cap = safe_find("Market Cap")

        return {
            "agent": "stealth/trendlyne_agent",
            "symbol": symbol,
            "source": url,
            "pe_ratio": pe_ratio or "N/A",
            "eps": eps or "N/A",
            "roe": roe or "N/A",
            "market_cap": market_cap or "N/A"
        }

    except Exception as e:
        return {
            "agent": "stealth/trendlyne_agent",
            "symbol": symbol,
            "error": str(e)
        }
