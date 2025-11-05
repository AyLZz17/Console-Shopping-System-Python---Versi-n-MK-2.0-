try:
    import datetime
    import os 
    from datetime import datetime  # Importación corregida
    from utils import utilidades as UT

except ImportError as e:
    print(f"Error al importar módulos: {e}")
    raise


def generar_recibo(carrito, total):
    """
    Genera y guarda un recibo de venta en formato de texto, mostrando además su contenido en consola.

    Flujo principal:
        1. Define la ruta base donde se guardarán los recibos generados.
        2. Crea un nombre único para el archivo de recibo utilizando la fecha y hora actual.
        3. Construye el contenido del recibo con los siguientes datos:
            - Encabezado del documento.
            - Lista detallada de productos comprados, incluyendo cantidad, precio unitario y subtotal.
            - Fecha y hora exacta de la transacción.
            - Total general a pagar.
        4. Guarda el recibo como archivo .txt en la ruta especificada.
        5. Muestra en consola el contenido del recibo y la confirmación de guardado mediante `UT.cuadro_verde()`.

    Parámetros:
        - carrito (dict): Diccionario con los productos comprados. 
            Estructura esperada:
                {
                    'nombre_producto': {
                        'precio': float,
                        'cantidad': int
                    },
                    ...
                }
        - total (float): Monto total de la compra, correspondiente a la suma de todos los subtotales.

    Dependencias:
        - datetime (módulo estándar): Para obtener la fecha y hora actuales.
        - os (módulo estándar): Para crear rutas de archivos y combinarlas correctamente.
        - UT (interfaz.utilidades): Para imprimir cuadros de texto y mensajes formateados.

    Efectos:
        - Crea un archivo de recibo con el detalle de la venta en formato de texto (.txt).
        - Muestra el recibo en consola junto con la ruta de guardado.
        - No retorna ningún valor.

    Ubicación del archivo generado:
        - Se almacena por defecto en:
          '\Proyectos Prog\Python\PROYECTO TIENDA\MK-2.0\Sistem\Data\Recibos'
        - Si la ruta está vacía, se guarda en el directorio raíz del módulo que ejecuta la función.

    Ejemplo de salida del archivo generado:
        ----- RECIBO DE VENTA ----
        Productos comprados:
        - Pan: 2 x $2000.00 = $4000.00
        - Leche: 1 x $3500.00 = $3500.00
        2025-10-27 21:38:41

        Total a pagar: $7500.00
        -------------------------
    """

#ruta donde se guarda el recibo generado
    ruta_relativa = r"..\MK-2.01\System\Data\Recibos"#Cambia dependiendo de donde este trabajando el proyecto (SI se deja en blanco el STR, SE GUARDA EN LA CARPETA RAIZ (Sistem))
    ruta_recibos = os.path.abspath(ruta_relativa) # Obtener ruta absoluta


#Parametros de nombre del archivo
    tiempo= datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
    nombre_archivo = f"recibo_{tiempo}.txt"

#Genera la ruta completa del archivo
    ruta_archivo = os.path.join(ruta_recibos, nombre_archivo) 

# Contenido del recibo
    contenido_recibo = '----- RECIBO DE VENTA ----\n'
    contenido_recibo += 'Productos comprados:\n'

    for nombre, datos in carrito.items():
        precio = datos['precio']
        cantidad = datos['cantidad']
        subtotal = precio * cantidad
        contenido_recibo += f'- {nombre}: {cantidad} x ${precio:.2f} = ${subtotal:.2f}\n'
        contenido_recibo += f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'

    contenido_recibo += f'\nTotal a pagar: ${total:.2f}\n'
    contenido_recibo += '-------------------------\n'

# Guardar el recibo en un archivo de texto
    with open(ruta_archivo, 'w') as archivo:
        archivo.write(contenido_recibo)

    # Mostrar el recibo en consola y la confirmacion de guardado
    UT.cuadro_verde(contenido_recibo)
    UT.cuadro_verde(f'Recibo generado: {ruta_archivo}')