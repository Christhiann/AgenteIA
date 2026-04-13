from app.agents.news_agent import agente_noticias


def decidir_acao(pergunta: str):
    pergunta = pergunta.lower()

    if any(p in pergunta for p in ["noticia", "notícias", "noticias", "news"]):
        return "noticias"
    
    if any(p in pergunta for p in ["previsao", "clima", "tempo"]):
        return "clima"
    
    return "chat"

def ask_ai(pergunta: str):
    try:
        acao = decidir_acao(pergunta)

        if acao == "noticias":
            return agente_noticias(pergunta)

        elif acao == "clima":
            return "🌤️ Clima ainda não implementado"

        return f"🤖 Você disse: {pergunta}"

    except Exception as e:
        return f"❌ Erro interno: {str(e)}"