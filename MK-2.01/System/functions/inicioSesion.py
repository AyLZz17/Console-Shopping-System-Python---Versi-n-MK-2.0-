import bcrypt 
import json
import time
import os
from utils import utilidades as UT


#apertura del archivo json donde se guardan los datos de registros de trabajadores
ruta_relativa = r"..\MK-2.01\System\Data\CredencialesTrabajadores.json"
# Obtener ruta absoluta a partir de relativa
ruta = os.path.abspath(ruta_relativa)

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
