# agents/news_agent.py
from app.config.settings import API_KEY  # importa a chave carregada

import requests

def extrair_tema(pergunta: str):
    palavras_remover = ["noticia", "noticias", "notícias", "sobre", "me", "traga", "as", "de"]
    palavras = pergunta.lower().split()
    tema = [p for p in palavras if p not in palavras_remover]
    return " ".join(tema)

def buscar_noticias(termo: str):
    if not API_KEY:
        return ["⚠️ API KEY não configurada"]

    url = f"https://newsapi.org/v2/everything?q={termo}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    artigos = data.get("articles", [])[:3]

    if not artigos:
        return ["⚠️ Nenhuma notícia encontrada"]

    noticias = [{"titulo": a.get("title"), "link": a.get("url")} for a in artigos]
    return noticias

def agente_noticias(pergunta: str):
    tema = extrair_tema(pergunta)
    noticias = buscar_noticias(tema)
    resposta = f"📰 Notícias reais sobre {tema}:\n\n"
    for n in noticias:
        if isinstance(n, dict):
            resposta += f"👉 {n['titulo']}\n🔗 {n['link']}\n\n"
        else:
            resposta += f"{n}\n"
    return resposta