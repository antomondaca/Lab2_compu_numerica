import os
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
    t_bolzano = "Si" if fa * fb < 0 else "No, tiene raíz doble"
    print(f"Intervalo: [{limite_izq}, {limite_der}], f(a) = {fa}, f(b) = {fb}, Teorema de Bolzano: {t_bolzano}")

    metodos = {
    "Bisección": biseccion(f, limite_izq, limite_der, tolerancia=tol, max_iteraciones=max_i, raiz_exacta=None),
    "Falsa Posición": falsa_posicion(f, limite_izq, limite_der, tolerancia=tol, max_iteraciones=max_i, raiz_exacta=None),
    "Punto Fijo": punto_fijo(f, g, aprox_actual, tolerancia=tol, max_iteraciones=max_i, raiz_exacta=None),
    "Newton Raphson": newton_raphson(f, df, aprox_actual, tolerancia=tol, max_iteraciones=max_i, raiz_exacta=None),
    "Newton Raphson Mejorado": newton_raphson_modificado(f, df, df2, aprox_actual, tolerancia=tol, max_iteraciones=max_i, raiz_exacta=None),
    "Secante": secante(f, aprox_antigua, aprox_actual, tolerancia=tol, max_iteraciones=max_i)
    }
