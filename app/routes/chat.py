from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.agents.news_agent import agente_noticias
from app.agents.orchestrator import decidir_acao
from app.services.memory import salvar_mensagem

router = APIRouter()

@router.post("/chat")
def chat(request: ChatRequest):

    salvar_mensagem(request.message)

    acao = decidir_acao(request.message)

    if acao == "noticias":
        resposta = agente_noticias(request.message)

    else:
        resposta = ask_ai(request.message)

    return {"response": resposta}