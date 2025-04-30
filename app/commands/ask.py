from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, CommandHandler, filters
from infra.external_services.ai_api import ask_question

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Use: /ask [sua pergunta]")
        return

    question = " ".join(context.args)
    await update.message.reply_text("Pensando... 🤔")
    answer = ask_question(question)
    await update.message.reply_text(answer)
