from telegram import InlineKeyboardButton, InlineKeyboardMarkup

async def handle(update, context):
    keyboard = [
        [
            InlineKeyboardButton("CS2", callback_data='cs2'),
            InlineKeyboardButton("LOL", callback_data='lol'),
            InlineKeyboardButton("FURIA FC", callback_data='furia_fc'),
            InlineKeyboardButton("Valorant", callback_data='valorant'),
            InlineKeyboardButton("Apex Legends", callback_data='apex_legends'),
            InlineKeyboardButton("PUBG Mobile", callback_data='pubg_mobile'),
            InlineKeyboardButton("Rocket League", callback_data='rocket_league'),
            InlineKeyboardButton("Rainbow Six Siege", callback_data='rainbow_six_siege'),
            InlineKeyboardButton("EA Sports FC", callback_data='ea_sports_fc'),
            InlineKeyboardButton("Free Fire", callback_data='free_fire'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text("Escolha a modalidade:", reply_markup=reply_markup)

async def button(update, context):
    query = update.callback_query
    query.answer()

    selected_modality = query.data

    if selected_modality == 'cs2':
        message = "Jogadores da FURIA em CS2: Player1, Player2, Player3, FalleN"
    elif selected_modality == 'lol':
        message = "Jogadores da FURIA em LOL: Player1, Player2, Player3"
    elif selected_modality == 'furia_fc':
        message = "Jogadores da FURIA FC: Jogador1, Jogador2, Jogador3"
    elif selected_modality == 'valorant':
        message = "Jogadores da FURIA em Valorant: Jogador1, Jogador2, Jogador3"
    elif selected_modality == 'apex_legends':
        message = "Jogadores da FURIA em Apex Legends: Jogador1, Jogador2, Jogador3"
    elif selected_modality == 'pubg_mobile':
        message = "Jogadores da FURIA em PUBG Mobile: Jogador1, Jogador2, Jogador3"
    elif selected_modality == 'rocket_league':
        message = "Jogadores da FURIA em Rocket League: Jogador1, Jogador2, Jogador3"
    elif selected_modality == 'rainbow_six_siege':
        message = "Jogadores da FURIA em Rainbow Six Siege: Jogador1, Jogador2, Jogador3"
    elif selected_modality == 'ea_sports_fc':
        message = "Jogadores da FURIA em EA Sports FC: Jogador1, Jogador2, Jogador3"
    elif selected_modality == 'free_fire':
        message = "Jogadores da FURIA em Free Fire: Jogador1, Jogador2, Jogador3"
    else:
        message = "Modalidade não reconhecida."

    await query.edit_message_text(text=message)
