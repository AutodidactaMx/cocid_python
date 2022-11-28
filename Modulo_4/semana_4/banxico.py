import matplotlib.pyplot as plt

import requests
import pandas as pd
import json
from types import SimpleNamespace

url = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/2013-01-01/2022-11-27?token=079c7118f780ea66ceb98180b0ef50ff38188df96a7e727547afa7831712c66a"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
x = json.loads(response.text)
#js_data = json.dumps(x.bmx.series[0].datos)
dato = x['bmx']['series'][0]['datos']
y = json.dumps(dato)
df = pd.read_json(y)
df['fecha'] = pd.to_datetime(df['fecha'])


df.plot.line(grid=True, marker='*', x='fecha',y='dato')


plt.show()