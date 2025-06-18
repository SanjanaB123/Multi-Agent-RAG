# config.py
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# llm = ChatOpenAI(model= 'gpt-4o-mini' ,temperature=0.2, openai_api_key=OPENAI_API_KEY, max_tokens=1200)