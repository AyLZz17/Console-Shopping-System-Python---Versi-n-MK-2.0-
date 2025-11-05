import os
import time

"""
Archivo: utilidades.py
Descripción:
    Este módulo proporciona funciones para mostrar cuadros de texto en la consola
    con colores ANSI. Es compatible con Windows, Linux y Mac. Permite destacar
    información mediante distintos colores: rojo, verde, amarillo/naranja, cyan y azul.

Funciones:
    clear()           - Limpia la pantalla de la consola.
    cuadro_naranja()  - Muestra un cuadro amarillo/naranja.
    cuadro_cyan()     - Muestra un cuadro cyan.
    cuadro_rojo()     - Muestra un cuadro rojo.
    cuadro_verde()    - Muestra un cuadro verde.
    cuadro_info()     - Muestra un cuadro de información (azul).
"""

# Colores ANSI
colores = [
    
    "\033[91m", # rojo
    "\033[92m", # verde
    "\033[93m", # amarillo/naranja
    "\033[94m", # azul
    "\033[95m", # magenta
    "\033[96m"  # cyan
]

reset = "\033[0m"

def clear():
    """Limpia la pantalla de la consola (compatible con Windows y Linux/Mac)."""
    os.system("cls" if os.name == "nt" else "clear")

def cuadro_naranja(texto):
    mostrar_cuadro(texto, colores[2])  # amarillo/naranja

def cuadro_cyan(texto):
    mostrar_cuadro(texto, colores[5])  # cyan

def cuadro_rojo(texto):
    mostrar_cuadro(texto, colores[0])  # rojo

def cuadro_verde(texto):
    mostrar_cuadro(texto, colores[1])  # verde

def cuadro_info(texto):
    # cuadro de informacion adicional
    mostrar_cuadro(texto, colores[3])  # azul

def mostrar_cuadro(texto, color): # Función para mostrar un cuadro de texto con un color específico
    """Función interna para dibujar un recuadro con color."""
    lineas = texto.split("\n")
    ancho = max(len(linea) for linea in lineas) + 4
    bordeArriba = "╔" + "═" * (ancho - 2) + "╗"
    bordeAbajo = "╚" + "═" * (ancho - 2) + "╝"

    print(color + bordeArriba)
    for linea in lineas:
        print(color + "║ " + linea.ljust(ancho - 4) + " ║")
    print(color + bordeAbajo + reset)
    time.sleep(1.2)
