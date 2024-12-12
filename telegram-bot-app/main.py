from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

from time import sleep

import requests
import json
import re
from datetime import datetime


# Importa o token da API
caminho_telegram_token = "C:/Users/jeffe/OneDrive/Área de Trabalho/Organização/Ciência/Portifolio/FutebolAPI-Bot/assets/telegram_token.txt"
caminho_vivo = "../FutebolAPI-Bot/info_live.txt"


# Importa o token da API
caminho_api = "C:/Users/jeffe/OneDrive/Área de Trabalho/Organização/Ciência/Portifolio/FutebolAPI-Bot/assets/token.txt"
with open(caminho_api, 'r') as arquivo: 
    token_api = arquivo.read()


def conteudo_api(link="/matches"):
    url = "https://api.football-data.org/v4"
    link_api = f"{url}{link}"

    # Faz a solicitação do conteúdo da API
    headers = {'X-Auth-Token': token_api}
    obj_api = requests.get(link_api, headers=headers)

    return obj_api.json()

# Usar regex pra converter as horas utc para utc-3
formato_hora = r"\d{2}:\d{2}:\d{2}"
formato_dia = r"\d{4}-\d{2}-\d{2}"

info_partidas = conteudo_api() # atualiza a API

with open("info_live.txt", "w", encoding="utf-8") as arquivo:
    for jogos in info_partidas['matches']:

        horas = re.findall(formato_hora, jogos['utcDate'])
        dias = re.findall(formato_dia, jogos['utcDate'])
        
        if dias[0] in jogos['utcDate'] and jogos['status'] == 'IN_PLAY':
            inicio_partida = f"{int(horas[0][0:2])-3}{horas[0][2:]}"
            inicio_partida = datetime.strptime(inicio_partida, "%H:%M:%S") #.time()
            agora = datetime.now()
            diferenca = agora - inicio_partida

            try:
                if jogos['referees'] != 0: 
                    arbitro = jogos['referees'][0]['name']
            except IndexError:
                arbitro = " Não informado "

            arquivo.write(f"\
Data do jogo: {dias[0]}\n\
Hora de inicio: {int(horas[0][0:2])-3}{horas[0][2:]}\n\
Situação da partida: AO VIVO\n\n\
\
Competição: {jogos['competition']['name']}\n\
Equipe de casa: {jogos['homeTeam']['name']}\n\
Equipe visitante: {jogos['awayTeam']['name']}\n\n\
\
Placar:\n\
{jogos['homeTeam']['name']} - {jogos['score']['fullTime']['home']} x {jogos['score']['fullTime']['away']} - {jogos['awayTeam']['name']}\n\
Arbitro: {arbitro}\n\
=================================\n\n")
        
        if dias[0] in jogos['utcDate'] and jogos['status'] == 'PAUSED':
            inicio_partida = f"{int(horas[0][0:2])-3}{horas[0][2:]}"
            inicio_partida = datetime.strptime(inicio_partida, "%H:%M:%S") #.time()
            agora = datetime.now()
            diferenca = agora - inicio_partida

            arquivo.write(f"\
Data do jogo: {dias[0]}\n\
Hora de inicio: {int(horas[0][0:2])-3}{horas[0][2:]}\n\
Situação da partida: INTERVALO\n\n\
\
Competição: {jogos['competition']['name']}\n\
Equipe de casa: {jogos['homeTeam']['name']}\n\
Equipe visitante: {jogos['awayTeam']['name']}\n\n\
\
Placar:\n\
{jogos['homeTeam']['name']} - {jogos['score']['fullTime']['home']} x {jogos['score']['fullTime']['away']} - {jogos['awayTeam']['name']}\n\
Arbitro: {arbitro}\n\
=================================\n\n")


# ======================== TELEGRAM BOT CODE ABAIXO ========================

with open(caminho_telegram_token, 'r') as arquivo: 
    TOKEN = arquivo.read()

def apresentacao(update: Update, context: CallbackContext) -> None:  

    keyboard = [
        [InlineKeyboardButton("🎥 AO VIVO", callback_data="VIVO")],
        [InlineKeyboardButton("🇧🇷 Brasileiro A", callback_data="BRA"), InlineKeyboardButton("🌎 Libertadores", callback_data="LAT")],
        [InlineKeyboardButton("🇫🇷 League One", callback_data="FRA"), InlineKeyboardButton("🇩🇪 Bundesliga", callback_data="ALE")],
        [InlineKeyboardButton("🇮🇹 Serie A", callback_data="ITA"), InlineKeyboardButton("🇳🇱 Heredivise", callback_data="HOL")],
        [InlineKeyboardButton("🇵🇹 Portugal", callback_data="POR"), InlineKeyboardButton("🇪🇦 La Liga", callback_data="ESP")],
        [InlineKeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League", callback_data="PL"), InlineKeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 Champioship", callback_data="CHA")],
        [InlineKeyboardButton("🌍 UEFA Champions League", callback_data="UEFA"), InlineKeyboardButton("🌍 Europa League", callback_data="EL")],
        [InlineKeyboardButton("🗺️ Copa do Mundo", callback_data="MUN")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard) 

    update.message.reply_text(
    '🔴 Atualizações ao vivo: Receba informações em tempo real sobre gols, substituições e outros eventos de partidas.\
    \n\n 📊 Estatísticas de times e jogadores: Consulte dados detalhados de desempenho.\
    \n\n 📅 Agenda de partidas: Veja datas e horários dos jogos dos seus times favoritos.\
    \n\n 🏆 Classificação de ligas: Acompanhe tabelas atualizadas dos campeonatos mais populares.\
    \n\n 🗂️ Pesquisa personalizada: Encontre informações sobre times, jogadores ou competições específicas.\
    \n\n=======================\nComo podemos te ajudar? '

    , reply_markup=reply_markup
    )
    # update.message.reply_text('Como podemos te ajudar?', reply_markup=reply_markup)



def botao(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'BRA':
        query.edit_message_text(text="Você escolheu Brasileirão A\
        \n\nNesta etapa de edição da msg, vc sempre exibe a msg final com as stats para o usuário")

    elif query.data == 'PL':
        
        keyboard = [
            [InlineKeyboardButton("🏆 Classificação", callback_data="RANK"),  InlineKeyboardButton("🚀 Top goleadores", callback_data="TOP")],
            [InlineKeyboardButton("📊 Head2Head", callback_data="H2H"), InlineKeyboardButton("⚽ Partidas", callback_data="PAR")],
            [InlineKeyboardButton("Inicio", callback_data="BACK")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard) 

        query.edit_message_text(text="Você escolheu a Premier League\
        \n\nComo podemos te ajudar?"
        , reply_markup=reply_markup)


    elif query.data == 'PAR':
        query.edit_message_text(text="Em breve, aparecerão as estatísticas das partidas aqui")

    elif query.data == 'TOP':
        query.edit_message_text(text="Em breve, aparecerão as estatísticas dos Top goleadores aqui")

    elif query.data == 'RANK':
        query.edit_message_text(text="Em breve, aparecerá a tabela de classificação aqui")

    elif query.data == 'H2H':
        query.edit_message_text(text="Em breve, aparecerão as estatísticas do Head2Head aqui")


    elif query.data == 'BACK':
        
        keyboard = [
        [InlineKeyboardButton("🎥 AO VIVO", callback_data="VIVO")],
        [InlineKeyboardButton("🇧🇷 Brasileiro A", callback_data="BRA"), InlineKeyboardButton("🌎 Libertadores", callback_data="LAT")],
        [InlineKeyboardButton("🇫🇷 League One", callback_data="FRA"), InlineKeyboardButton("🇩🇪 Bundesliga", callback_data="ALE")],
        [InlineKeyboardButton("🇮🇹 Serie A", callback_data="ITA"), InlineKeyboardButton("🇳🇱 Heredivise", callback_data="HOL")],
        [InlineKeyboardButton("🇵🇹 Portugal", callback_data="POR"), InlineKeyboardButton("🇪🇦 La Liga", callback_data="ESP")],
        [InlineKeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League", callback_data="PL"), InlineKeyboardButton("🏴󠁧󠁢󠁥󠁮󠁧󠁿 Champioship", callback_data="CHA")],
        [InlineKeyboardButton("🌍 UEFA Champions League", callback_data="UEFA"), InlineKeyboardButton("🌍 Europa League", callback_data="EL")],
        [InlineKeyboardButton("🗺️ Copa do Mundo", callback_data="MUN")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard) 

        query.edit_message_text(
        '🔴 Atualizações ao vivo: Receba informações em tempo real sobre gols, substituições e outros eventos de partidas.\
        \n\n 📊 Estatísticas de times e jogadores: Consulte dados detalhados de desempenho.\
        \n\n 📅 Agenda de partidas: Veja datas e horários dos jogos dos seus times favoritos.\
        \n\n 🏆 Classificação de ligas: Acompanhe tabelas atualizadas dos campeonatos mais populares.\
        \n\n 🗂️ Pesquisa personalizada: Encontre informações sobre times, jogadores ou competições específicas.\
        \n\n=======================\nComo podemos te ajudar? '

        , reply_markup=reply_markup
        )


    elif query.data == 'VIVO':
        keyboard=[
            [InlineKeyboardButton("💎 Clube Black 💎", callback_data="BET")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard) 
        
        with open(caminho_vivo, 'r', encoding="utf-8") as arquivo:
            query.edit_message_text(
                text=arquivo.read()
                )
            

                



    else:
        query.edit_message_text(text="Bot em construção!")




def main(): 
    updater = Updater(TOKEN) 
    dispatcher = updater.dispatcher 

    dispatcher.add_handler(CommandHandler("start", apresentacao)) 
    dispatcher.add_handler(CallbackQueryHandler(botao))
    
    updater.start_polling() 
    updater.idle() 


if __name__ == '__main__':
    main()