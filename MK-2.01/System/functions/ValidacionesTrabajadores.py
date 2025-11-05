try:
    
    from functions import reportes as rep, GestionProductos as GDP
    from utils import utilidades as UT
    import time 
    import json
    import bcrypt
    import os

except ImportError as e:
    print(f"Error al importar módulos: {e}")
    raise

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

def opciones_trabajador():
    """
    Muestra y gestiona el menú principal de opciones disponibles para los trabajadores.
    Flujo principal:
        1. Despliega un menú con las siguientes opciones:
            - (1) Añadir productos: Permite registrar o actualizar productos en el inventario.
            - (2) Crear reportes: Genera un reporte de ventas con estadísticas generales.
            - (3) Eliminar productos: Elimina un producto existente del inventario.
            - (4) Cerrar sesión: Sale del menú de trabajador y regresa al menú principal.
        2. El menú se ejecuta en un bucle continuo hasta que el usuario seleccione la opción “4”.
        3. Cada opción limpia la consola antes de ejecutar su acción correspondiente.

    Dependencias:
        - UT (interfaz.utilidades): Para limpiar la consola y mostrar cuadros de texto con formato.
        - GDP (GestionProductos): Para las funciones de añadir y eliminar productos.
        - rep (reportes): Para la generación de reportes de ventas.
        - time: Para pausar brevemente en caso de errores o mensajes informativos.

    Efectos:
        - Modifica el inventario de productos mediante `añadirProductos()` o `eliminar_productos()`.
        - Puede generar un reporte de ventas en formato `.txt` mediante `rep.generar_reportes()`.
        - Mantiene interacción constante con el usuario por consola.

    Ejemplo de flujo de uso:
        - Trabajador selecciona "1": Añade un nuevo producto al inventario.
        - Trabajador selecciona "2": Se genera y guarda un reporte de ventas.
        - Trabajador selecciona "3": Elimina un producto existente.
        - Trabajador selecciona "4": Finaliza la sesión y regresa al menú principal.
    """

    while True:
        UT.clear()
        UT.cuadro_verde("""--- MENÚ TRABAJADOR ---

1. Añadir productos
2. Crear reportes
3. Eliminiar productos
4. Cerrar sesión
""")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                UT.clear()
                GDP.añadirProductos()
            case "2":
                UT.clear()
                rep.generar_reportes()
            case "3":
                UT.clear()
                GDP.eliminar_productos()
            case "4":
                UT.cuadro_rojo("Cerrando sesión... ")
                time.sleep(1)
                break
            case _:
                UT.cuadro_rojo(" Opción no válida, por favor intente nuevamente.")
                time.sleep(1)


def registrar_usuario():
    """
Registra un nuevo usuario en el sistema, validando previamente las credenciales de un administrador.

Flujo principal:
    1. Solicita al usuario ingresar las credenciales de administrador (usuario y contraseña).
    2. Verifica que las credenciales correspondan a un usuario con rol "ADMINISTRADOR DEL PROGRAMA" en el diccionario `usuarios`.
    3. Si la validación es correcta:
        - Solicita los datos del nuevo usuario: nombre, contraseña y rol (admin/trabajador).
        - Valida la complejidad de la contraseña (mínimo 8 caracteres, al menos una letra y un número).
        - Genera un hash seguro de la contraseña usando bcrypt.
        - Agrega el nuevo usuario al diccionario `usuarios` con su contraseña hasheada y su rol.
        - Guarda los cambios en el archivo JSON correspondiente.
        - Muestra un mensaje de confirmación en consola.
    4. Si la validación falla:
        - Informa que las credenciales del administrador son incorrectas y no realiza ningún cambio.

Parámetros:
    - usuarios (dict): Diccionario que contiene los usuarios actuales con sus contraseñas y roles.
    - ruta (str): Ruta del archivo JSON donde se almacenan los datos de los usuarios.

Efectos:
    - Modifica el archivo JSON de usuarios agregando un nuevo registro.
    - Interactúa con el usuario por consola solicitando y mostrando información.
    - Utiliza bcrypt para el cifrado seguro de contraseñas.

Ejemplo de flujo de uso:
    - Admin ingresa: usuario = "admin01", contraseña = "clave123".
    - Se valida correctamente.
    - Ingresa nuevo usuario: nombre = "juan", clave = "pass456", rol = "trabajador".
    - Se registra el nuevo usuario y se guarda en el archivo JSON.
"""

    print("\n--- Registro de usuario ---\n")
    nombre_admin = input("Usuario administrador: ")
    clave_admin = input("Contraseña administrador: ")

    if nombre_admin in usuarios and usuarios[nombre_admin]["rol"] == "ADMINISTRADOR DEL PROGRAMA":
        hash_guardado = usuarios[nombre_admin]["password"].encode("utf-8")
        clave_admin_bytes = clave_admin.encode("utf-8")

        if bcrypt.checkpw(clave_admin_bytes, hash_guardado):
            nuevo_usuario = input("Ingrese el nombre del nuevo usuario: ")
            nueva_clave = input("Ingrese la contraseña del nuevo usuario: ")

            if len(nueva_clave) < 8:
                print("La contraseña debe tener al menos 8 caracteres.")
            elif not any(char.isdigit() for char in nueva_clave):
                print("La contraseña debe contener al menos un número.")
            elif not any(char.isalpha() for char in nueva_clave):
                print("La contraseña debe contener al menos una letra.")
            else:
                print("Contraseña válida.")

                # convertir contraseña en un arrgelo de bytes
                bytes = nueva_clave.encode('utf-8')

                # Generar Salt (medida de seguridad)
                salt = bcrypt.gensalt()

                # Hasheo de la contraseña
                hash = bcrypt.hashpw(bytes, salt)


                rol_usuario = input("Ingrese el rol del nuevo usuario (admin/trabajador): ")

                usuarios[nuevo_usuario] = {"password": hash.decode('utf-8'), "rol": rol_usuario}

                #añadir datos nuevos al archivo .JSON
                with open(ruta, "w") as archivo:
                    json.dump(usuarios, archivo, indent=4)

                print(f"Usuario '{nuevo_usuario}' registrado exitosamente con rol '{rol_usuario}'.")
    else:
        print("Credenciales de administrador incorrectas.")

def login():
    """
    Inicia sesión en el sistema verificando las credenciales de un usuario registrado.

    Flujo principal:
        1. Solicita al usuario ingresar su nombre de usuario y contraseña.
        2. Comprueba si el nombre existe en el diccionario `usuarios` y si la contraseña coincide.
        3. Si las credenciales son válidas:
            - Muestra un mensaje de bienvenida junto con el rol del usuario.
            - Espera brevemente antes de continuar.
            - Retorna `True` indicando un inicio de sesión exitoso.
        4. Si las credenciales no coinciden:
            - Muestra un mensaje de error.
            - Espera brevemente antes de continuar.
            - Retorna `False` indicando un fallo en la autenticación.

    Parámetros:
        - usuarios (dict): Diccionario que contiene los usuarios registrados, junto con sus contraseñas y roles.

    Retorna:
        - bool: `True` si el inicio de sesión es exitoso, `False` en caso contrario.

    Efectos:
        - Interactúa con el usuario mediante la consola.
        - Introduce un breve retraso (2 segundos) tras mostrar los mensajes para mejorar la legibilidad.

    Ejemplo de flujo de uso:
        - Usuario ingresa: nombre = “admin01”, contraseña = “clave123”.
        - Si las credenciales son correctas, se muestra:
              “Bienvenido, admin01. Rol: admin”
        - Si son incorrectas, se muestra:
              “Usuario o contraseña incorrectos.”
    """
    print("\n--- Inicio de sesión ---")
    nombre = input("Usuario: ")
    clave = input("Contraseña: ")

    if nombre in usuarios:
        # Convertimos el hash almacenado (texto) y la contraseña ingresada a bytes
        hash_guardado = usuarios[nombre]["password"].encode('utf-8')
        clave_bytes = clave.encode('utf-8')

        # Verificar si la contraseña ingresada coincide con el hash guardado
        if bcrypt.checkpw(clave_bytes, hash_guardado):
            print(f"Bienvenido, {nombre}. Rol: {usuarios[nombre]['rol']}")
            time.sleep(1)
            return True
        else:
            print("Usuario o contraseña incorrectos.")
            time.sleep(1)
            return False
    else:
        print("Usuario o contraseña incorrectos.")
        time.sleep(1)
        return False
