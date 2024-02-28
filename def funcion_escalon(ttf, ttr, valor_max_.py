
def funcion_escalon(ttf, ttr, valor_max_MW: int):
    tiempo_total = 8736
    resultado = []
    acumulado = 0
    escalon_actual = valor_max_MW

    for i, j in zip(sorted(ttf), sorted(ttr)):
        # Mantener el escalón en valor_max_MW hasta el primer valor de ttf
        resultado.extend([escalon_actual] * int(i))
        acumulado += i
        
        # Caer a cero durante el tiempo de ttr
        resultado.extend([0] * int(j))
        acumulado += j

        escalon_actual = valor_max_MW  # Volver a subir a valor_max_MW al llegar al último valor de ttr

        # if acumulado >= tiempo_total:
        #     break

    return resultado

print(funcion_escalon([1,2,3,],[3,4,5],5))
