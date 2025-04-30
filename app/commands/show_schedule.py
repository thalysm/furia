from datetime import datetime
from telegram import Update

async def handle(update: Update, context):
    # Simulando um calendário de jogos para a FURIA
    games_schedule = [
        {"date": "2025-05-01", "game": "FURIA vs Team A (CS2)"},
        {"date": "2025-05-05", "game": "FURIA vs Team B (LOL)"},
        {"date": "2025-05-10", "game": "FURIA vs Team C (FURIA FC)"},
    ]

    # Obtendo a data de hoje
    today = datetime.today().strftime('%Y-%m-%d')

    # Filtrando os jogos que ocorrerão após hoje
    upcoming_games = [game for game in games_schedule if game["date"] >= today]

    # Formatação da mensagem de resposta
    if upcoming_games:
        message = "Próximos jogos da FURIA:\n"
        message += "\n".join([f"{game['date']} - {game['game']}" for game in upcoming_games])
    else:
        message = "Não há jogos programados para o futuro."

    # Enviando a resposta para o usuário
    await update.message.reply_text(message)
