def biseccion(f, limite_izq, limite_der, tolerancia=1e-6, max_iteraciones=100):
    if f(limite_izq) * f(limite_der) >= 0: # Teorema de Bolzano
        return None, 0, [], False
    historial = [] # Almacena el historial de errores k-esimos para las graficas
    c_ant = limite_izq # Valor referencial inciial para calcular el error absoluto
    for k in range(1, max_iteraciones + 1):  
        punto_medio = (limite_izq + limite_der) / 2 # Divvidimos el intervalo a la mitad osea, punto medio
        error = abs(punto_medio - c_ant) if k > 1 else abs(limite_der - limite_izq)  # Calculamos el error absoluto
        historial.append(error)
        if abs(f(punto_medio)) < tolerancia or error < tolerancia: # Criterio de parada
            return punto_medio, k, historial, True # Retarna: raiz, iteraciones, erorres, exito
        if f(limite_izq) * f(punto_medio) < 0: # Reduccion de intervalo
            limite_der = punto_medio # Si esta entre a y c, acotamos el intervalo por la derecha, por lo tanto b = c
        else:
            limite_izq = punto_medio # Si esta entre c y b, acotamos el intervalo por la izquierda, por lo tanto a = c
        c_ant = punto_medio # Se guarda el punto medio actual
    return punto_medio, max_iteraciones, historial, False
        