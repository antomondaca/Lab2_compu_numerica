import numpy as np

def punto_fijo():
    historial = []
    valor_esti_anterior = valor_inicial 

    for i in range(1, max_iteraciones + 1): #Evaluamos la funcion por si hay raices negativas
        valor_esti_actual = g(valor_esti_anterior)
        error = abs(valor_esti_actual - valor_esti_anterior)
        historial.append(error)

        if np.isnan(valor_esti_actual) or np.isinf(valor_esti_actual): #Por si la funcion diverge
            print("La función g(x) no converge a un valor finito.")
            return None, i, historial, False
        
        if error < tolerancia: # Criterio de parada
            return valor_esti_actual, i, historial, True
        valor_esti_actual = valor_esti_anterior

    return valor_esti_actual, max_iteraciones, historial, False