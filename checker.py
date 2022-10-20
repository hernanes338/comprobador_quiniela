import results_history, players_bets

jornada_comprobacion = 14

resultado = results_history.list_resultados[jornada_comprobacion - 1]['combinacion']

signos = resultado[:-2]

pleno15 = resultado[-2:]

list_aciertos = []

for i in range(len(players_bets.list_pronosticos)):
    aciertos = 0
    pronostico = players_bets.list_pronosticos[i]['pronostico']

    #comprobacion signos (1X2)
    for j in range(len(signos)):
        if pronostico[j] == signos[j]:
            aciertos += 1
    
    # comprobacion pleno al 15 (012M)
    if aciertos == 14 and pleno15 == pronostico[-2:]:
        aciertos += 1

    list_aciertos.append(
        {'jornada': jornada_comprobacion,
        'jugador': players_bets.list_pronosticos[i]['jugador'],
        'aciertos': aciertos,
        'pronostico': players_bets.list_pronosticos[i]['pronostico']})

print(list_aciertos)