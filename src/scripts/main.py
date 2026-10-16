import os
import csv
import numpy as np

from biseccion import biseccion
from falsa_posicion import falsa_posicion
from punto_fijo import punto_fijo
from new_raphson import newton_raphson
from newton_mejorado import newton_raphson_modificado
from secante import secante
from funciones import Funciones
from graficos import graficos

# Garantizar que las carpetas requeridas estén presentes
directorio_actual = os.path.dirname(os.path.abspath(__file__))
carpeta_data = os.path.abspath(os.path.join(directorio_actual, "..", "data"))
os.makedirs(carpeta_data, exist_ok=True)

tol = 1e-6 # Variable gobal de la tolerancia
max_i = 100 # Variable global del maximo de iteraciones
resultados = []

for clave, info in Funciones.items():
    f = info["f"]
    df = info["df"]
    df2 = info["d2f"]
    g = info["g"]
    limite_izq = info["a"]
    limite_der = info["b"]
    aprox_actual = info["x0"]
    aprox_antigua = info["x1"]
    fa = f(limite_izq)
    fb = f(limite_der)
    t_bolzano = "Si" if fa * fb < 0 else "Raíz doble"
    print(f"Intervalo: [{limite_izq}, {limite_der}], f(a) = {fa}, f(b) = {fb}, Teorema de Bolzano: {t_bolzano}")

    x = np.linspace(limite_izq, limite_der, 150) # Archivo csv por función con columnas (x,f(x))
    y = f(x)
    ruta_csv = os.path.join(carpeta_data, f"curva_{clave}.csv")
    with open(ruta_csv, mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["x", "f(x)"])
        writer.writerows(zip(np.round(x, 5), np.round(y, 5)))

    ruta_csv_resumen = os.path.join(carpeta_data, "resumen_convergencia.csv") # Archvio resumen de convergencias
    with open(ruta_csv_resumen, mode="w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Funcion", "Metodo", "Raiz", "Iteraciones", "Error_Final", "Estado"])
        writer.writerows(resultados)
    
    metodos = {
    "Bisección": biseccion(f, limite_izq, limite_der, tol, max_i, raiz_exacta=None),
    "Falsa Posición": falsa_posicion(f, limite_izq, limite_der, tol, max_i, raiz_exacta=None),
    "Punto Fijo": punto_fijo(f, g, aprox_actual, tol, max_i, raiz_exacta=None),
    "Secante": secante(f, aprox_antigua, aprox_actual, tol, max_i, raiz_exacta=None),
    "Newton Raphson": newton_raphson(f, df, aprox_actual, tol, max_i, raiz_exacta=None),
    "Newton Raphson Mejorado": newton_raphson_modificado(f, df, df2, aprox_actual, tol, max_i, raiz_exacta=None)
}

resultados_convergencia = {}
raiz_encontrada = None

for nom_metodo, (raiz, iteraciones, errores, vof) in metodos.items():
    if len(errores) > 0:
        errores_final = errores[-1]
    else:
        errores_final = None

    if vof:
        estado = "Convergió"
    elif raiz is None:
        estado = "No aplica" # Cuando no cumple con algun requerimiento de algun metodo
    else:
        estado = "Falló" # Falla cuando no llega a la tolerancia

    if raiz is not None:
        raiz_str = f"{raiz:.6f}" # Muestra la raiz con 6 decimales
    else:
        raiz_str = "N/A"

    if errores_final is not None:
        errores_str = f"{errores_final:.2e}" # Muestra con notacion cientifica 
    else:
        errores_str = "N/A"

    resultados.append([clave, nom_metodo, raiz_str, iteraciones, errores_str, estado])

    if vof: # Si el metodo tuvo exito, se guarda para graficar
        if raiz_encontrada is None:
            raiz_encontrada = raiz
    
    resultados_convergencia[nom_metodo] = {
        "historial": errores,
        "exito": vof
    }


