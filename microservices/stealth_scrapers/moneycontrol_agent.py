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


from playwright.sync_api import sync_playwright

def scrape_moneycontrol(symbol: str, browser_type='chromium') -> dict:
    url = f"https://www.moneycontrol.com/india/stockpricequote/{symbol.lower()}"
    try:
        with sync_playwright() as p:
            browser = getattr(p, browser_type).launch(headless=True)
            context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
            page = context.new_page()
            page.goto(url, timeout=60000)
            content = page.content()
            # You'd parse actual content here (example below returns dummy)
            return {
                "agent": f"stealth/moneycontrol_agent_{browser_type}",
                "symbol": symbol,
                "price": "1000",
                "eps": "40",
                "pe": "25"
            }
    except Exception as e:
        return {
            "agent": f"stealth/moneycontrol_agent_{browser_type}",
            "symbol": symbol,
            "error": str(e)
        }

def run(symbol: str):
    return scrape_moneycontrol(symbol, browser_type='chromium')  # Change to 'firefox' to use Mozilla
