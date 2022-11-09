import results_history, bets_history

list_resultados = results_history.list_resultados

list_pronosticos = bets_history.list_pronosticos

jornada_comprobacion = ''

resultado = ''

for i in range(len(list_resultados)):
    if list_resultados[i]['jornada'] != jornada_comprobacion:
        continue
    else: 
        resultado = list_resultados[i]['combinacion']
        break

signos = resultado[:-2]

pleno15 = resultado[-2:]

list_aciertos = []

for i in range(len(list_pronosticos)):
    
    if list_pronosticos[i]['jornada'] != jornada_comprobacion:
        continue
    else:
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
                
            list_aciertos.append(
                {'jornada': jornada_comprobacion,
                'jugador': jugador,
                'aciertos': aciertos,
                'pronostico': pronostico})

for i in range(len(list_aciertos)):
    print(list_aciertos[i])


        