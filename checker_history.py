import results_history, bets_history

list_resultados = results_history.list_resultados

list_pronosticos = bets_history.list_pronosticos

jornadas_con_pronosticos = []

for i in range(len(list_pronosticos)):
    jornadas_con_pronosticos.append(list_pronosticos[i]['jornada'])

list_aciertos = []

for i in range(len(list_pronosticos)):
    jornada = list_pronosticos[i]['jornada']
    resultado = ''
    signos = ''
    pleno15 = ''
    list_aciertos.append({'jornada': jornada})

    for x in range(len(list_resultados)):
        if list_pronosticos[i]['jornada'] == list_resultados[x]['jornada']:
            resultado = list_resultados[x]['combinacion']
            signos = resultado[:-2]
            pleno15 = resultado[-2:]
            break

    for j in range(len(list_pronosticos[i]['pronosticos'])):
        aciertos = 0
        jugador = list_pronosticos[i]['pronosticos'][j]['jugador']
        pronostico = list_pronosticos[i]['pronosticos'][j]['pronostico']
        
        for k in range(len(signos)):
            
            if pronostico[k] == signos[k]:
                aciertos += 1

        # comprobacion pleno al 15 (012M)
        if aciertos == 14 and pleno15 == pronostico[-2:]:
            aciertos += 1

        if resultado != '': 
            list_aciertos.append(
                {'jugador': jugador,
                'aciertos': aciertos,
                'pronostico': pronostico})

for i in range(len(list_aciertos)):
    print(list_aciertos[i])
