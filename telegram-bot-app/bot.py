from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler
from time import sleep

TOKEN = '7707442510:AAEpdauv3Q71T_kHS_3f6QqWv0IAO0ji7eI'

handlers = {}
texto_voltar = 'Voltar'

msg_pagamento = "Processando pagamento..."

# Configurações da mensagem inicial
msg_inicial = {
'keyboard_inicial' : [
        [InlineKeyboardButton("⚽ Partidas Hoje", callback_data="partida_hoje")],
        [InlineKeyboardButton("🎥 AO VIVO", callback_data="in_live")],
        [InlineKeyboardButton("🇧🇷 Brasileirão A", callback_data="BSA"), InlineKeyboardButton("🌎 Libertadores", callback_data="CLI")],
        [InlineKeyboardButton("🇫🇷 League 1", callback_data="FL1"), InlineKeyboardButton("🇩🇪 Bundesliga", callback_data="BL1")],
        [InlineKeyboardButton("🇮🇹 Serie A", callback_data="SA"), InlineKeyboardButton("🇳🇱 Eredivise", callback_data="DED")],
        [InlineKeyboardButton("🇵🇹 Primeira Liga", callback_data="PPL"), InlineKeyboardButton("🇪🇦 La Liga", callback_data="PD")],
        [InlineKeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League", callback_data="PL"), InlineKeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 Champioship", callback_data="ELC")],
        [InlineKeyboardButton("🌍 UEFA Champions League", callback_data="CL"), InlineKeyboardButton("🌍 Europa League", callback_data="EC")],
        [InlineKeyboardButton("🗺️ Copa do Mundo", callback_data="WC")]
    ],
'texto_inicial' : '🔴 Atualizações ao vivo.\
\n\n 📊 Estatísticas de times e jogadores.\
\n\n 📅 Agenda de partidas.\
\n\n 🏆 Classificação de ligas.\
\n\n 🗂️ Pesquisa personalizada.\
\n\n=======================\nPrepare-se para as principais ligas do futebol - Premier League, Serie A, La Liga, Bundesliga, Ligue 1, \
Champions Leeague e outras.'
}


# Decorator
def botao(nome):
    def decorator(func):
        handlers[nome] = func
        return func
    return decorator


@botao("partida_hoje")
def handle_partida_hoje(update, context):
    # Receber conteudo da API

    keyboard = [
        [InlineKeyboardButton(f"🔝{texto_voltar}🔝", callback_data="BACK")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query.edit_message_text(
        "Informações sobre partidas hoje", reply_markup=reply_markup
        )


@botao("in_live")
def handle_in_live(update, context):
    keyboard = [
        [InlineKeyboardButton(f"🔝{texto_voltar}🔝", callback_data="BACK")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query.edit_message_text(
        "Informações sobre partidas AO VIVO", reply_markup=reply_markup
        )


@botao("BACK")
def handle_voltar(update, context):
    reply_markup = InlineKeyboardMarkup(msg_inicial['keyboard_inicial'])

    update.callback_query.edit_message_text(
            msg_inicial['texto_inicial']
        , reply_markup=reply_markup
        )


@botao("PAR")
def handle_partida(update, context):
    for partida in range(2):
        keyboard = [
            [InlineKeyboardButton("📊 Head2Head", callback_data="H2H")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.callback_query.message.reply_text(
            f"Informações sobre a partida {partida+1}", reply_markup=reply_markup
            )
        sleep(0.5)

    keyboard = [
        [InlineKeyboardButton("🔥Clube Black🔥", callback_data="VIP")],
        [InlineKeyboardButton(f"🔝{texto_voltar}🔝", callback_data="BACK")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query.message.reply_text(text='Tenha acesso a relatórios profissionais e previsão de resultados feito\
 pelo melhor algoritmo de inteligência artificial otimizado para o futebol no \n\n🔥Clube Black🔥.',
        reply_markup=reply_markup
        )
    
    # sleep(2)

    # chat_id = update.message.chat_id
    # # Substitua 'STICKER_FILE_ID' pelo ID do seu sticker animado
    # sticker_file_id = 'CAACAgEAAxkBAAPGZ1hC75Tl6RhPYIK3yr61j6eWXL4AAkoDAAJv1xhE1FIWNP_ah4M2BA'
    # context.bot.send_sticker(chat_id=chat_id, sticker=sticker_file_id)


@botao("RANK")
def handle_rank(update, context):
    keyboard = [
        [InlineKeyboardButton(f"🔝{texto_voltar}🔝", callback_data="BACK")],
        [InlineKeyboardButton("🔥Clube Black🔥", callback_data="VIP")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query.edit_message_text(
        "Tabela de classificação\n==========\n\
 1. | Man. City\n\
 2. | Arsenal\n\
 3. | Man. United\n\
        ", reply_markup=reply_markup
        )


@botao("TOP")
def handle_top(update, context):
    keyboard = [
        [InlineKeyboardButton(f"🔝{texto_voltar}🔝", callback_data="BACK")],
        [InlineKeyboardButton("🔥Clube Black🔥", callback_data="VIP")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query.edit_message_text(
        "Top goleadores\n==========\n\
 1. | Neymar\n\
 2. | Messi\n\
 3. | Ronaldo\n\
        ", reply_markup=reply_markup
        )


@botao("H2H")
def handle_h2h(update, context):
    keyboard = [
        [InlineKeyboardButton(f"🔝{texto_voltar}🔝", callback_data="BACK")],
        [InlineKeyboardButton("🔥Clube Black🔥", callback_data="VIP")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query.edit_message_text(
        "Informações sobre os últimos confrontos das equipes", reply_markup=reply_markup
        )


@botao("VIP")
def handle_vip(update, context):
    keyboard = [
        [InlineKeyboardButton("1 mês R$29,90", callback_data="PRECO1")],
        [InlineKeyboardButton("6 meses R$159,90", callback_data="PRECO2")],
        [InlineKeyboardButton("1 ano R$329,90", callback_data="PRECO3")],
        [InlineKeyboardButton(f"🔝{texto_voltar}🔝", callback_data="BACK")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.callback_query.edit_message_text(
        "Escolha o melhor plano e tenha vantagens usando a nossa ferramenta de análise quantitativa\
 desenvolvida com inteligência artificial.", reply_markup=reply_markup
        )


@botao("PRECO1")
def handle_pagamento_1(update, context):
    update.callback_query.edit_message_text(
    text=msg_pagamento
    )


@botao("PRECO2")
def handle_pagamento_2(update, context):
    update.callback_query.edit_message_text(
    text=msg_pagamento
    )


@botao("PRECO3")
def handle_pagamento_3(update, context):
    update.callback_query.edit_message_text(
    text=msg_pagamento
    )

def callback_handler(update, context):
    query_data = update.callback_query.data
    
    keyboard = [
        [InlineKeyboardButton("🏆 Classificação", callback_data="RANK"),  InlineKeyboardButton("🚀 Top goleadores", callback_data="TOP")],
        [InlineKeyboardButton("📊 Head2Head", callback_data="H2H"), InlineKeyboardButton("⚽ Partidas", callback_data="PAR")],
        [InlineKeyboardButton(f"🔝{texto_voltar}🔝", callback_data="BACK")],
        [InlineKeyboardButton("🔥Clube Black🔥", callback_data="VIP")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    handlers.get(query_data, lambda u, c: u.callback_query.edit_message_text("Aproveite os nossos serviços gratuitos\nComo podemos ajudar?",
     reply_markup=reply_markup))(update, context)




def start(update, context):
    reply_markup = InlineKeyboardMarkup(msg_inicial['keyboard_inicial'])

    update.message.reply_text(
        msg_inicial['texto_inicial']
        , reply_markup=reply_markup)


def main():
    updater = Updater(TOKEN)
    updater.dispatcher.add_handler(CallbackQueryHandler(callback_handler))
    updater.dispatcher.add_handler(CommandHandler("campeonatos", start))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()