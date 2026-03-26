from fastapi import FastAPI
from app.routes import chat, predict

app = FastAPI(title="IA API Project", )
app.include_router(chat.router)
app.include_router(predict.router)

@app.get("/")
def home():
    return {"message": "Bem-vindo à IA API!"}


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)