import pandas as pd
import requests
import json

api = "https://api.football-data.org/v4"
url = f"{api}/matches"


with open('../FutebolAPI-Bot/assets/token.txt', 'r') as arquivo: 
    token = arquivo.read()


headers = { 'X-Auth-Token': token}

obj_api = requests.get(url, headers=headers)


with open("partidas.json", 'w') as arquivo: 
    json.dump(obj_api.json(), arquivo, indent=4)




