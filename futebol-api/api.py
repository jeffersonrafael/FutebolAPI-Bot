import pandas as pd
import requests
from requests.auth import HTTPBasicAuth

api = "https://api.football-data.org/v4"
url = f"{api}/matches"
headers = { 'X-Auth-Token': '24d761476ef14724a2593d62dfa91e57' }

obj_api = requests.get(url, headers=headers)


for match in obj_api.json()['matches']:
  print(match)

# if obj_api.status_code == 200:
#     print(obj_api.json())


