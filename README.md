# Evaluación de Laboratorio 2: La raíz que se esconde

Ramo: Computación Numérica INF- 123

Integrantes: 
- Antonella Mondaca
- Luis Manzur

## Descripción del Proyecto

Este repositorio contiene el desarrollo de la Evaluación 2, cuyo objetivo es implementar y comparar seis métodos de búsqueda de raíces, los cuales son:

- Bisección
- Falsa Posición
- Punto Fijo
- Secante
- Newton-Raphson
- Newton-Raphson Mejorado

Con estos metodos analizamos distintas funciones(polinómicas, logarítmicas, exponenciales, trigonométricas y mixtas), incluyendo el análisis crítico de una función con raíz doble que solo toca el eje x.

## Estructura del Repositorio

De acuerdo a la rúbrica solicitada, el proyecto se organiza de la siguiente manera:

- scripts/ o src/: Contiene todos los scripts de Python con la implementación de los métodos y las funciones.

- assets/: Carpeta donde se guardan los gráficos generados en formato PNG (funciones con sus raíces y gráficos de convergencia).

- data/: Contiene los archivos CSV generados por cada función con los datos (x, f(x)) y el resumen de convergencia.

- informe.md: Documento con las respuestas a las preguntas de convergencia y la conclusión argumentada.

- requirements.txt: Lista de dependencias necesarias (numpy, matplotlib).

## Configuración del Entorno Virtual (venv)

Para ejecutar este proyecto, utilizamos un entorno virtual local de Python. Esto nos permite aislar las dependencias del proyecto sin afectar la instalación global de Python en tu sistema.

### 1) Crear el entorno virtual

Desde la raíz del repositorio, abre tu terminal y ejecuta el siguiente comando para crear el entorno en una carpeta llamada env/:

En Windows, Linux o macOS:
``` bash
python -m venv 
```
>(Nota: La carpeta env/ debe estar ignorada en tu .gitignore para no subirla al repositorio).

### 2) Activar el entorno

Debes activar el entorno antes de instalar las dependencias o correr los scripts:

En Linux / macOS:
```
source env/bin/activate
```

En Windows:
```
env\Scripts\activate
```

Una vez activado, verás (env) al inicio de la línea de comandos de tu terminal.

### 3) Instalar dependencias

Con el entorno activado, instala las librerías requeridas ejecutando:
```
pip install -r requirements.txt
```

Esto instalará numpy para los cálculos numéricos y matplotlib para la generación de gráficos.

### 4) Ejecución del Código

Una vez que el entorno está activo y las dependencias instaladas, puedes ejecutar los scripts ubicados en la carpeta scripts/ (o src/). Por ejemplo:
```
python scripts/main.py
```

(Asegúrate de ajustar el nombre del archivo al script principal que utilicen).

>Nota sobre gráficos: Si estás corriendo los scripts en un entorno sin interfaz gráfica, recuerda que matplotlib guardará los gráficos directamente en la carpeta assets/ usando savefig() en lugar de mostrarlos en pantalla con show().

### 5) Desactivar el entorno

Cuando termines de trabajar, puedes salir del entorno virtual simplemente ejecutando:
```
deactivate
```