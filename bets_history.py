import json

with open('bets_history.json') as f:
   json_res = json.load(f)

list_pronosticos = []

for i in range(len(json_res)):
    list_pronosticos.append(json_res[i])

