import requests
from datetime import date, timedelta

inicio_temporada = '20220814' # jornada 1 de la temporada 2022-2023
ultima_jornada_completada = '20991231'
# ultima_jornada_completada = str(date.today() - timedelta(days=2)).replace("-","")

query = {'game_id':'LAQU', 'fechaInicioInclusiva': inicio_temporada, 'fechaFinInclusiva': ultima_jornada_completada} # , 'celebrados':'true' no parece afectar en nada
response = requests.get('https://www.loteriasyapuestas.es/servicios/buscadorSorteos', params=query)
json_res = response.json()

list_resultados = []

for i in range(len(json_res)-1, -1, -1):
    if not json_res[i]['combinacion']: # evita generar error si para una jornada aun no se ha publicado la combinacion de resultados
        continue
    list_resultados.append({'jornada': json_res[i]['jornada'], 'combinacion': json_res[i]['combinacion'].replace(" - ","")})