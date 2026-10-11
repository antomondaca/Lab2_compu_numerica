def secante(f, aprox_antigua, aprox_actual, tolerancia=1e-6, max_iteraciones=100):
    historial = []  # Almacena el historial de errores k-esimos para las graficas

    for i in range (1, max_iteraciones + 1): 
        y_antiguo, y_actual = f(aprox_antigua), f(aprox_actual)
        desnivel = y_actual - y_antiguo
        
        if abs(desnivel) < 1e-14:  # Evita la division por cero
            return None, i, historial, False
        nueva_aprox = aprox_actual - y_actual * (aprox_actual - aprox_antigua) / desnivel
        distancia = abs(nueva_aprox - aprox_actual) # Calculamos el error
        historial.append(distancia)

        if abs(f(nueva_aprox)) < tolerancia or distancia < tolerancia: # Criterio de parada
            return nueva_aprox, i, historial, True
        aprox_antigua = aprox_actual
        aprox_actual = nueva_aprox
    return nueva_aprox, max_iteraciones, historial, False