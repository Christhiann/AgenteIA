from openai import OpenAI

from app.config.settings import openai_api_key

client = OpenAI(api_key=openai_api_key)

def ask_openai(prompt: str):
    return f"Resposta simulada da IA para: {prompt}"