import requests
import pandas as pd


url = "https://timeapi.io/api/Time/current/zone" 
parameters = {"timeZone": "Asia/Seoul"}          

response = requests.get(url, params=parameters)
print(response.text) 

import json
js = json.loads(response.text)
print(js['year'])
