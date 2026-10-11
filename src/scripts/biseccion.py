def biseccion(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0: # Teorema de Bolzano
        return None, 0, [], False
    historial = [] # Almacena el historial de errores k-esimos para las graficas
    c_ant = a # Valor referencial inciial para calcular el error absoluto
    for k in range(1, max_iter + 1):  
        c = (a + b) / 2 # Divvidimos el intervalo a la mitad osea, punto medio
        error = abs(c - c_ant) if k > 1 else abs(b - a)  # Calculamos el error absoluto
        historial.append(error)
        if abs(f(c)) < tol or error < tol: # Criterio de parada
            return c, k, historial, True # Retarna: raiz, iteraciones, erorres, exito
        if f(a) * f(c) < 0: # Reduccion de intervalo
            b = c # Si esta entre a y c, acotamos el intervalo por la derecha, por lo tanto b = c
        else:
            a = c # Si esta entre c y b, acotamos el intervalo por la izquierda, por lo tanto a = c
        c_ant = c # Se guarda el punto medio actual
    return c, max_iter, historial, False
        