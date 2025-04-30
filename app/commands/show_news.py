from telegram import Update
from telegram.ext import ContextTypes
from infra.external_services.news_api import get_latest_news

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    news = get_latest_news()

    if not news:
        await update.message.reply_text("Não encontrei nenhuma notícia sobre a FURIA no momento.")
        return

    message = "📰 *Últimas notícias sobre a FURIA:*\n\n"

    for item in news:
        message += f"• [{item['title']}]({item['link']})\n📅 _{item['published']}_\n\n"

    await update.message.reply_markdown(message)
