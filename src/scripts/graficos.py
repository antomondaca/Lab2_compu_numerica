import os
import matplotlib.pyplot as plt
import numpy as np

# Creamos la ruta para guardar los graficos en src/assets/
directorio_actual = os.path.dirname(os.path.abspath(__file__))
carpeta_assets = os.path.join(directorio_actual, "..", "assets")
os.makedirs(carpeta_assets, exist_ok=True)

def graficar_curva(clave, datos_f, raiz):  
    plt.figure(figsize=(8,5))

    x_min, x_max = datos_f["lims"] # Creamos 500 puntos para que la linea se vea mas suave
    x = np.linspace(x_min, x_max, 500)
    y = datos_f["f"](x)

    plt.plot(x, y, label=datos_f["nombre"], color="blue", linewidth=2)
    plt.axhline(0, color="black", linestyle="--", linewidth=1, alpha=0.7)

    if raiz is not None:
        y_raiz = datos_f["f"](raiz)
        if datos_f["es_doble"]: # Aclaramos cuando es doble raiz y que es con tangente
            plt.plot(
                raiz,
                y_raiz,
                "ro",
                markersize=8,
                label=f"Raiz doble (Tangente): x ≈ {raiz:.4f}",
            )
        else:
            plt.plot(
                raiz,
                y_raiz,
                "ro",
                markersize=8,
                label=f"Raiz (Corte): x ≈ {raiz:.4f}",
            )

    plt.title(
        f"Comportamiento de la funcion: {datos_f['nombre']}", fontsize=12
    )
    plt.xlabel("x", fontsize=10)
    plt.ylabel("f(x)", fontsize=10)
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.legend()

    # Guardamos el grafico en assets
    ruta_guardado = os.path.join(carpeta_assets, f"curva_{clave}.png")
    plt.savefig(ruta_guardado, dpi=300, bbox_inches="tight")
    plt.close()

    def graficar_convergencia(clave, nombre_f, resultados_metodos):
        plt.figure(figsize=(9,6))

        estilos = { # Le damos distintos estilos a cada metodo
            "Biseccion": {"color": "tab:blue", "marker": "o"},
            "Falsa Posicion": {"color": "tab:orange", "marker": "s"},
            "Punto Fijo": {"color": "tab:green", "marker": "^"},
            "Secante": {"color": "tab:red", "marker": "v"},
            "Newton-Raphson": {"color": "tab:purple", "marker": "D"},
            "Newton-Raphson Mejorado": {"color": "tab:brown", "marker": "P"},
        }

        grafico_vacio = True

        for metodo, resultado in resultados_metodos.items(): # resultado cotiene: (raiz, iteraciones, historial, exito)
            historial = resultado["historial"]
            exito = resultado["exito"]

            if exito and len(historial) > 0: # Solo graficamos si es que el metodo convergio al final y tiene un historial
                grafico_vacio = False
                iteraciones = np.arange(1, len(historial) + 1)
                formato = estilos.get(metodo, {"color": "black", "marker": "x"})

                plt.plot(
                    iteraciones,
                    historial,
                    label=f"{metodo} ({len(historial)} iters)",
                    color=formato["color"],
                    marker=formato["marker"],
                    linewidth=1.5,
                    markersize=5,
                )
        
        if not grafico_vacio:
            ruta_guardado = os.path.join(
                        carpeta_assets, f"convergencia_{clave}.png"
                    )
            plt.savefig(ruta_guardado, dpi=300, bbox_inches="tight")
            pass

        plt.close()

    def graficar_resumen_iteraciones():
        pass