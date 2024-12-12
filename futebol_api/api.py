import requests
import json
import re
from datetime import datetime

# Importa o token da API
caminho = "C:/Users/jeffe/OneDrive/Área de Trabalho/Organização/Ciência/Portifolio/FutebolAPI-Bot/assets/token.txt"
# caminho = "../Portifolio/FutebolAPI-Bot/assets/token.txt"
# '../FutebolAPI-Bot/assets/token.txt'
with open(caminho, 'r') as arquivo: 
    token_api = arquivo.read()


def conteudo_api(link="/matches"):
    url = "https://api.football-data.org/v4"
    link_api = f"{url}{link}"

    # Faz a solicitação do conteúdo da API
    headers = {'X-Auth-Token': token_api}
    obj_api = requests.get(link_api, headers=headers)

    return obj_api.json()


def main():
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



if __name__ == '__main__':
    main()

