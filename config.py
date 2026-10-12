import os

from dotenv import load_dotenv

load_dotenv()


def get_google_api_key() -> str:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Google API key not found. Set GOOGLE_API_KEY in your environment or .env file."
        )
    return api_key