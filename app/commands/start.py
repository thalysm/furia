# app/commands/start.py

from telegram import Update
from telegram.ext import ContextTypes

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👊 Bem-vindo ao FanFuriaBot!\n\n"
        "Aqui você acompanha tudo sobre os times da FURIA em um só lugar!\n\n"
        "📋 Comandos disponíveis:\n"
        "/start - Ver essa mensagem de boas-vindas\n"
        "/collections - Veja a nossa útima coleção \n"
        "/news - Ver as últimas notícias da FURIA\n"
        "/schedule - Ver a agenda de partidas\n"
        "/players - Ver informações sobre jogadores por modalidade\n"
        "/ask - Faça perguntas sobre a Fúria\n"
        "/cheer - Enviar uma mensagem de apoio ao time 🖤\n\n"
        "Fique à vontade para explorar e apoiar a alcateia!"
    )
