
import logging
from datetime import datetime

logging.basicConfig(
    filename='monitoring.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s - %(message)s'
)

def log_event(source: str, action: str, metadata: dict = None):
    message = f"[{source}] {action}"
    if metadata:
        message += f" | META: {metadata}"
    logging.info(message)

def log_error(source: str, error: Exception):
    logging.error(f"[{source}] ERROR: {str(error)}")
