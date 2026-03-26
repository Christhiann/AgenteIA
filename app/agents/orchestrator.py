def decidir_acao(pergunta: str):
    pergunta = pergunta.lower()

    if any(p in pergunta for p in ["noticia", "notícias", "noticias", "news"]):
        return "noticias"
    
    if any(p in pergunta for p in ["previsao", "clima", "tempo"]):
        return "clima"
    
    return "chat"