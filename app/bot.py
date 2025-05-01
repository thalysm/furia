from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from app.commands import show_schedule, show_news, show_players, cheer, start, collections, ask
from app.config import TELEGRAM_TOKEN

def run_bot():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("schedule", show_schedule.handle))
    app.add_handler(CommandHandler("news", show_news.handle))
    app.add_handler(CommandHandler("players", show_players.handle))
    app.add_handler(CallbackQueryHandler(show_players.button))
    app.add_handler(CommandHandler("cheer", cheer.handle))
    app.add_handler(CommandHandler("start", start.handle))
    app.add_handler(CommandHandler("collections", collections.handle))
    app.add_handler(CommandHandler("ask", ask.handle))

    print("Bot está rodando...")
    app.run_polling()
