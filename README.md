# 🐍 FURIA Tech Bot – Desafio Técnico

Bot conversacional feito em Python + Telegram para o desafio técnico da vaga de Assistente de Engenharia de Software da FURIA Tech.  
O bot permite que fãs acompanhem o time com informações de partidas, elenco, notícias e interação divertida.

---

## 🧠 Funcionalidades

- `/start`: Mensagem de boas-vindas e lista de comandos.
- `/schedule`: Mostra os próximos jogos da FURIA (base fictícia).
- `/players`: Exibe os jogadores e permite escolher a modalidade (CS2, LoL, FURIA FC).
- `/news`: Lista as últimas notícias da FURIA (buscando do Google News).
- `/cheer`: Manda uma mensagem de torcida personalizada com emojis.
- `/collections`: Anuncia a última coleção lançada (ex: Adidas Collab).
- `/ask`: Faz perguntas para a IA (utilizando modelo local via Ollama).

---

## 🧱 Estrutura (Clean Architecture)

```
furia/
├── main.py                         # Entrypoint do bot
├── assets/
│   └── images/                     # Imagens
├── app/
|   ├── config.py                   # Configurações (token etc)
│   └── commands/                   # Handlers dos comandos
│       ├── cheer.py
│       ├── show_news.py
│       ├── show_players.py
│       ├── show_schedule.py
│       ├── ask.py
│       ├── collections.py
│       └── start.py
├── infra/
│   └── external_services/          # Integrações com APIs externas
│       ├── ai_api.py
│       └── news_api.py
├── domain/
│   └── models.py                   # Modelos de dados
├── requirements.txt                # Dependências
├── Dockerfile
├── docker-compose.yml
└── .dockerignore
```

---

## 🚀 Como rodar localmente (modo simples)

1. **Clone o repositório**
```bash
git clone https://github.com/thalysm/furia.git
cd furia
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Configure o token no arquivo `config.py`**
```python
TELEGRAM_TOKEN = "SEU_TOKEN_DO_BOT"
```

4. **Execute o bot**
```bash
python main.py
```

---

## 🐳 Como rodar com Docker

> Requer [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados.

1. **Configure o arquivo `.env`** com sua chave do Telegram:
```env
TELEGRAM_TOKEN=seu_token_aqui
```

2. **Suba os containers**
```bash
docker-compose up --build
```

3. **Baixe o modelo LLM dentro do container Ollama**
```bash
docker exec -it ollama ollama pull llama3
```

> O serviço `furia_bot` já estará apontando para `http://ollama:11434`, funcionando com IA local.

---

## 📹 Demonstração

O vídeo de apresentação com as interações pode ser assistido [aqui](#).

---

## 👨‍💻 Tecnologias

- Python 3.10+
- python-telegram-bot v20+
- Feedparser
- Clean Architecture
- Ollama (via Docker, com modelo LLaMA3)

---

## 📁 Observações

- Algumas respostas usam dados mockados (jogadores, partidas), mas as notícias são carregadas de um feed real.
- O projeto pode ser facilmente estendido com conexão a banco de dados ou APIs da própria FURIA.
- A IA funciona localmente, sem custo com a OpenAI, graças ao uso do [Ollama](https://ollama.com/).