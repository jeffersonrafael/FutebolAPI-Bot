import pandas as pd
import requests
from requests.auth import HTTPBasicAuth
import json

api = "https://api.football-data.org/v4"
url = f"{api}/matches"
headers = { 'X-Auth-Token': '24d761476ef14724a2593d62dfa91e57' }

obj_api = requests.get(url, headers=headers)


with open("partidas.json", 'w') as arquivo: 
    json.dump(obj_api.json(), arquivo, indent=4)




