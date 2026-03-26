import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
API_KEY = os.getenv("NEWS_API_KEY")