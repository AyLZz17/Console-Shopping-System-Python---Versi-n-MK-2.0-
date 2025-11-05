try:

    import json
    import os
    from utils import utilidades as UT
    from functions import GestionProductos as GDP

except ImportError as e:
    print(f"Error al importar módulos: {e}")
    raise


ruta_relativa = r"../Data/Productos.json"

RUTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), ruta_relativa)

def cargar_productos():
    """
    Carga los productos almacenados en el archivo JSON especificado por la ruta RUTA.

    Verifica si el archivo existe y contiene datos válidos antes de intentar cargarlo.
    Si el archivo no existe, está vacío o contiene un formato JSON inválido, retorna
    un diccionario vacío para evitar errores en la ejecución.

    Returns:
        dict: Diccionario con los productos cargados desde el archivo JSON.
        Retorna un diccionario vacío si no hay datos válidos.
    """
    
    if not os.path.exists(RUTA) or os.stat(RUTA).st_size == 0:
        return {}
    try:
        with open(RUTA, "r") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return {}

def guardar_productos(productos):
    """Guarda el diccionario de productos en el archivo JSON especificado por la ruta RUTA.

    Sobrescribe el contenido anterior del archivo con los datos actuales de los productos,
    manteniendo el formato legible mediante indentación.

    Args:
        productos (dict): Diccionario que contiene los productos a guardar, donde
        cada clave es el nombre del producto y su valor es otro
        diccionario con los campos 'id', 'precio' y 'cantidad'.
    """
    
    with open(RUTA, "w") as archivo:
        json.dump(productos, archivo, indent=4)

def añadirProductos():
    """
    Permite registrar o actualizar productos en el inventario del sistema.

    Flujo del proceso:
        1. Limpia la pantalla y muestra el encabezado del módulo.
        2. Carga los productos existentes desde el archivo JSON.
        3. Solicita al usuario los datos del nuevo producto:
            - Nombre del producto.
            - ID (formato XXX###).
            - Precio (valor numérico).
            - Cantidad en stock (entero).
        4. Si el producto ya existe:
            - Actualiza su precio, ID y suma la nueva cantidad al stock existente.
        5. Si el producto no existe:
            - Lo añade como un nuevo registro en el archivo.
        6. Guarda los cambios en el archivo JSON y muestra un mensaje de confirmación.
        7. Si ocurre un error de tipo de dato (por ejemplo, valores no numéricos), 
           muestra un mensaje de error y no guarda cambios.

    Efectos:
        - Modifica el archivo de productos (`Productos.json`) actualizando o añadiendo registros.
        - Muestra mensajes en consola mediante la interfaz de utilidades (UT).

    Dependencias:
        - `UT` (interfaz.utilidades): para mostrar mensajes en pantalla.
        - `cargar_productos()`: para leer los datos actuales del inventario.
        - `guardar_productos()`: para guardar los cambios realizados.

    Excepciones:
        - ValueError: si el usuario ingresa valores no válidos en precio o cantidad.

    """
    
    UT.clear()
    UT.cuadro_naranja("AÑADIR PRODUCTOS")

    productos = cargar_productos()

    try:
        nombre = input("Ingrese el nombre del producto: ").strip().lower()
        id_producto = input("Ingrese el ID del producto (formato XXX###): ").strip().upper()
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad en STOCK: "))

        if nombre in productos:
            UT.cuadro_naranja(
                f"El producto '{nombre}' ya existe. Se actualizará el stock y el precio."
            )
            productos[nombre]["cantidad"] += cantidad
            productos[nombre]["precio"] = precio
            productos[nombre]["id"] = id_producto
        else:
            productos[nombre] = {"id": id_producto, "precio": precio, "cantidad": cantidad}

        guardar_productos(productos)

        UT.cuadro_verde(
            f"Producto '{nombre}' añadido/actualizado exitosamente.\n"
            f"ID: {productos[nombre]['id']} | Precio: ${precio:.2f} | Cantidad total: {productos[nombre]['cantidad']}"
        )

    except ValueError:
        UT.cuadro_rojo(
            "Error: Solo puedes ingresar números válidos.\n"
            "Ejemplo cantidad: 1000 | Ejemplo precio: 299.99"
        )

def eliminar_productos():

    """
    Permite eliminar un producto del inventario existente, identificándolo por nombre o por ID.

    Flujo del proceso:
        1. Limpia la pantalla y muestra el encabezado del módulo.
        2. Carga los productos registrados desde el archivo JSON.
        3. Si no hay productos registrados, muestra un mensaje y finaliza la ejecución.
        4. Muestra en pantalla un listado con todos los productos disponibles, incluyendo:
            - Nombre
            - ID
            - Precio
            - Cantidad en stock
        5. Solicita al usuario el nombre o el ID del producto que desea eliminar.
        6. Busca el producto:
            - Primero intenta coincidir por nombre.
            - Si no lo encuentra, busca por ID.
        7. Si el producto existe:
            - Solicita confirmación antes de eliminarlo.
            - Si el usuario confirma (opción "s"):
                - Elimina el producto del diccionario.
                - Actualiza el archivo JSON llamando a `guardar_productos()`.
                - Muestra mensaje de confirmación.
            - Si el usuario cancela, muestra un aviso y no realiza cambios.
        8. Si no se encuentra el producto, muestra un mensaje de error.

    Efectos:
        - Modifica el archivo `Productos.json`, eliminando el producto seleccionado.
        - Imprime en consola los mensajes correspondientes mediante la interfaz de utilidades (UT).

    Dependencias:
        - `UT` (interfaz.utilidades): para limpiar pantalla y mostrar mensajes.
        - `cargar_productos()`: para obtener el inventario actual.
        - `guardar_productos()`: para guardar los cambios tras la eliminación.

    Excepciones:
        - No lanza errores. Si el archivo JSON no existe o está vacío, el proceso se detiene controladamente.

    """
    
    UT.clear()
    UT.cuadro_naranja("ELIMINAR PRODUCTOS")

    productos = cargar_productos()

    if not productos:
        UT.cuadro_rojo("No hay productos registrados para eliminar.")
        return
    
    # Mostrar lista de productos disponibles
    UT.clear()
    menu_texto = "=== MENÚ DE PRODUCTOS DISPONIBLES ===\n"
    for nombre, datos in productos.items():
        menu_texto += f"- {nombre.title()} | ID: {datos['id']} | Precio ${datos['precio']} | Cantidad: {datos['cantidad']}\n"
    menu_texto += "=================================================================================\n"
    UT.cuadro_cyan(menu_texto)

    # Solicitar producto a eliminar (por nombre o ID)
    entrada = input("Ingrese el NOMBRE o el ID del producto a eliminar: ").strip().lower()

    # Buscar por nombre
    if entrada in productos:
        nombre = entrada
    else:
        # Buscar por ID
        nombre = None
        for prod, datos in productos.items():
            if datos.get("id", "").lower() == entrada:
                nombre = prod
                break

    if nombre:
        confirmacion = input(f"¿Seguro que desea eliminar '{nombre}'? (s/n): ").strip().lower()
        if confirmacion == "s":
            del productos[nombre]
            guardar_productos(productos)
            UT.cuadro_verde(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            UT.cuadro_naranja("Eliminación cancelada.")
    else:
        UT.cuadro_rojo(f"No se encontró ningún producto con el nombre o ID '{entrada}'.")



productos = cargar_productos() #carga los productos al iniciar el modulo
