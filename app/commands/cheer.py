import random

async def handle(update, context):
    cheers = [
        "🔥 VAMOS FURIAAAAAAA 🔥#DIADEFURIA",
        "FURIA É O TIME DO CORAÇÃO!",
        "FURIA, A FORÇA DO BRASIL!",
        "VAI FURIA! RUMO À VITÓRIA!",
        "FURIA, O ORGULHO DO BRASIL!",
        "FURIA, SEMPRE NA LUTA!",
        "FURIA, O TIME QUE NUNCA DESISTE!",
        "FURIA, A GLÓRIA É NOSSA!",
    ]

    cheer = random.choice(cheers)
    await update.message.reply_text(cheer)


