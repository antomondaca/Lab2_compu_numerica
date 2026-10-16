import numpy as np

def new_raphson(f, df, df2, aprox_actual, tolerancia=1e-6, max_iteraciones=100, raiz_exacta=None):
    historial = []
    
    for i in range(1, max_iteraciones + 1):
        y = f(aprox_actual)
        dy = df(aprox_actual)
        d2y = df2(aprox_actual) # Todo lo mismo del new_raphson pero esto es nuevo

        if np.abs(dy) < 1e-14: # Caso en el que la derivada es 0 o casi 0
            return None, i, np.array(historial), False

        numerador = y * dy
        denominador = dy ** 2 - (y * d2y)
        nueva_aprox = aprox_actual - (numerador / denominador)
        y_nueva = f(nueva_aprox)

        if raiz_exacta is not None: # Calculamos el error
            diferencia = np.abs(nueva_aprox - raiz_exacta)
        else:
            diferencia = np.abs(nueva_aprox - aprox_actual)

        historial.append(diferencia)

        if np.abs(y_nueva) < tolerancia or diferencia < tolerancia: # Criterio de parada
            return nueva_aprox, i, np.array(historial), True

        aprox_actual = nueva_aprox

    return nueva_aprox, max_iteraciones, np.array(historial), False