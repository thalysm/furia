from telegram import Update, InputFile, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    caption = (
        "*FURIA | ADIDAS*\n\n"
        "*RESPEITO É PRA QUEM TEM!*\n\n"
        "Vem garantir o manto mais querido e aguardado...\n\n"
        "As três listras mais famosas do esporte se uniram à nossa pantera, "
        "e você não vai querer ficar fora desse time.\n\n"
        "*DESENVOLVIDA PARA O SEU MÁXIMO DESEMPENHO:*\n\n"
        "Esta não é apenas uma camiseta.\n"
        "É um manto que vai te acompanhar em todos os momentos. 🖤🐾"
    )

    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("🛒 Ver Coleção", url="https://www.furia.gg/produtos/collabs/adidas")
    ]])

    with open("assets/images/furia_adidas_collection.png", "rb") as image:
        await update.message.reply_photo(
            photo=InputFile(image),
            caption=caption,
            parse_mode="Markdown",
            reply_markup=keyboard
        )
