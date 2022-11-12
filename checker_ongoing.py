import requests

inicio_temporada = '20220814' # jornada 1 de la temporada 2022-2023
ultima_jornada_completada = '20991231'

query = {'game_id':'LAQU', 'fechaInicioInclusiva': inicio_temporada, 'fechaFinInclusiva': ultima_jornada_completada} # , 'celebrados':'true' no parece afectar en nada
response = requests.get('https://www.loteriasyapuestas.es/servicios/buscadorSorteos', params=query)
json_res = response.json()

partidos = json_res[0]['partidos']
resultado = []

for partido in partidos:
   resultado.append(partido['signo'])

signos = resultado[:14]

pleno15 = resultado[14:]

# introducir pronostico para la jornada en marcha
pronostico = ''

aciertos = 0

for i in range(len(signos)):
    if signos[i] == pronostico[i]:
        aciertos += 1
    
# comprobacion pleno al 15 (012M)
if aciertos == 14 and pleno15 == pronostico[-2:]:
    aciertos += 1

print(aciertos)