
import os
from dotenv import load_dotenv

load_dotenv()

def validate_token(token: str):
    AUTH_TOKEN = os.getenv("ALPHA_API_TOKEN")
    return token == AUTH_TOKEN
