import numpy as np

def falsa_posicion(f, limite_izq, limite_der, tolerancia=tol, max_iteraciones=max_i, raiz_exacta=None):
    fa = f(limite_izq)
    fb = f(limite_der)

    if fa * fb >= 0: # Teorema de Bolzano
        return None, 0, [], False
    
    historial = [] # Almacena el historial de errores k-esimos para las graficas
    c_ant = limite_izq # Valor referencial para el error absoluto

    for k in range(1, max_iteraciones + 1):  
        punto_medio = (limite_izq * fb - limite_der * fa) / (fb - fa) # Formula de la falsa posicion
        fc = f(punto_medio)

        # (falta calculo del error absoluto)

        if np.abs(fc) < tolerancia or error < tolerancia: # Criterio de parada
            return punto_medio, k, np.array(historial), True # Retorna: raiz, iteraciones, errores, exito
        
        if fa * fc < 0: # Reduccion de intervalo
            limite_der = punto_medio 
            fb = fc
        else:
            limite_izq = punto_medio
            fa = fc
            
        c_ant = punto_medio # Se guarda el punto medio actual
        
    return punto_medio, max_iteraciones, np.array(historial), False