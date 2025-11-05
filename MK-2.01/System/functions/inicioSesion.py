import bcrypt 
import json
import time
import os
from utils import utilidades as UT


# Ruta relativa
ruta_relativa = r"../Data/CredencialesTrabajadores.json" 

# Obtener la ruta absoluta usando la carpeta del script actual
ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), ruta_relativa)



usuarios = {}
try:
    with open(ruta, "r") as archivo:
        contenido = archivo.read().strip()
        if contenido:
            usuarios = json.loads(contenido)
        else:
            usuarios = {}
except (json.JSONDecodeError, FileNotFoundError):
    usuarios = {}
 
def inicio_sesion_main():

    print("\n--- Inicio de sesión ---")
    # Verificar que la ruta resultante sea correcta
    print(f"Ruta del archivo: {ruta}")
    nombre = input("Usuario: ")
    clave = input("Contraseña: ")
    continuar = input("Presione Enter para continuar")

    if nombre in usuarios:
        # Convertimos el hash almacenado (texto) y la contraseña ingresada a bytes
        hash_guardado = usuarios[nombre]["password"].encode('utf-8')
        clave_bytes = clave.encode('utf-8')

        # Verificar si la contraseña ingresada coincide con el hash guardado
        if bcrypt.checkpw(clave_bytes, hash_guardado):
            print(f"Bienvenido, {nombre}. Rol: {usuarios[nombre]['rol']}")
            time.sleep(2.3)
            return True
        else:
            print("Contraseña incorrectos.")
            time.sleep(2.3)
            return False
    else:
        print("Usuario incorrecto.")
        time.sleep(2.3)
        return False
