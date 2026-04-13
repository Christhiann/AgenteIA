# IA API Project

## Descrição do Projeto

Este projeto é uma API de Inteligência Artificial (IA) desenvolvida com FastAPI no backend e React no frontend. O sistema permite interações via chat com agentes de IA, incluindo um agente de notícias que busca informações em tempo real usando a NewsAPI, e um serviço de predição (atualmente placeholder para análise de imagens médicas). O frontend oferece uma interface de chat simples para interagir com a API.

O projeto foi criado para demonstrar integrações com serviços de IA e APIs externas, utilizando uma arquitetura modular com agentes especializados e serviços de memória.

## Funcionalidades

- **Chat com IA**: Interface de chat que permite enviar mensagens e receber respostas de agentes de IA.
- **Agente de Notícias**: Detecta perguntas relacionadas a notícias e busca artigos relevantes usando a NewsAPI.
- **Orquestrador de Ações**: Decide qual agente usar baseado em palavras-chave na mensagem do usuário (notícias, clima, ou chat geral).
- **Serviço de Predição**: Endpoint para predições (atualmente simulado para detecção de câncer em imagens).
- **Histórico de Mensagens**: Armazenamento simples em memória das mensagens enviadas.
- **Frontend React**: Interface web para interação com a API via chat.

## Tecnologias Utilizadas

### Backend (Python/FastAPI)
- **FastAPI**: Framework web para construção da API REST.
- **Pydantic**: Para validação e serialização de dados (modelos de request/response).
- **Requests**: Para fazer chamadas HTTP à NewsAPI.
- **OpenAI Python SDK**: Integração com a API da OpenAI (atualmente placeholder/simulado).
- **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.

### Frontend (React)
- **React**: Biblioteca para construção da interface de usuário.
- **Axios**: Cliente HTTP para fazer requisições à API backend.
- **React Scripts**: Ferramentas de build e desenvolvimento para React.
- **Testing Library**: Para testes unitários e de integração.

### Integrações
- **OpenAI API**: Para geração de respostas de IA (simulado no código atual).
- **NewsAPI**: Para busca de notícias em tempo real.
- **CORS Middleware**: Para permitir requisições do frontend ao backend.

### Outros
- **Git**: Controle de versão.
- **Virtual Environment (venv)**: Ambiente virtual Python para isolamento de dependências.
- **NPM**: Gerenciador de pacotes para o frontend.

## Arquitetura do Projeto

O projeto segue uma estrutura modular:

- **app/main.py**: Ponto de entrada da aplicação FastAPI, configuração de rotas e middleware CORS.
- **app/routes/**: Endpoints da API (chat.py para chat, predict.py para predições).
- **app/agents/**: Agentes especializados (news_agent.py para notícias, orchestrator.py para decidir ações).
- **app/services/**: Serviços utilitários (openai_service.py para OpenAI, model_service.py para predições, memory.py para histórico).
- **app/models/**: Modelos de dados (schemas.py com Pydantic).
- **app/config/**: Configurações (settings.py para chaves de API).
- **frontend/**: Aplicação React para interface web.

## Instalação e Configuração

### Pré-requisitos
- Python 3.8+
- Node.js 14+
- Chaves de API: NewsAPI e OpenAI (configurar em `app/config/settings.py`)

### Backend
1. Clone o repositório e navegue para a pasta do projeto.
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente: `venv\Scripts\activate` (Windows) ou `source venv/bin/activate` (Linux/Mac)
4. Instale as dependências: `pip install fastapi uvicorn requests openai pydantic`
5. Configure as chaves de API em `app/config/settings.py` (arquivo pode precisar ser criado).
6. Execute o servidor: `uvicorn app.main:app --reload`

### Frontend
1. Navegue para a pasta `frontend`.
2. Instale as dependências: `npm install`
3. Execute o frontend: `npm start`

A aplicação backend rodará em `http://127.0.0.1:8000` e o frontend em `http://localhost:3000`.

## Uso

1. Inicie o backend e o frontend conforme instruções acima.
2. Abra o navegador em `http://localhost:3000`.
3. Digite uma mensagem no chat (ex: "notícias sobre tecnologia" para ativar o agente de notícias).
4. O sistema responderá com notícias ou uma resposta simulada da IA.

### Endpoints da API
- `GET /`: Mensagem de boas-vindas.
- `POST /chat`: Envia uma mensagem e recebe resposta do agente apropriado.
- `GET /predict`: Retorna uma predição simulada.

## Desenvolvimento e Contribuição

- O projeto usa Git para controle de versão.
- Testes podem ser adicionados usando pytest para backend e Testing Library para frontend.
- Para contribuir, faça um fork, crie uma branch e submeta um pull request.

## Notas

- O serviço de OpenAI está atualmente simulado; para uso real, configure a chave de API e implemente a chamada completa.
- O serviço de predição é um placeholder; pode ser expandido para integração com modelos de ML reais (ex: TensorFlow, PyTorch).
- O histórico de mensagens é armazenado em memória; para produção, considere um banco de dados.
- Certifique-se de configurar as variáveis de ambiente ou o arquivo settings.py com as chaves de API necessárias.

## Licença

Este projeto é de código aberto. Consulte o arquivo LICENSE para mais detalhes.
