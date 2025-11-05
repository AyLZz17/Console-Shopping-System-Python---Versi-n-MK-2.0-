try:
    from utils import utilidades as UT
    from collections import defaultdict
    import os
    from datetime import datetime
except ImportError as e:    
    print(f"Error al importar módulos: {e}")
    raise

historial_ventas = []


def registrar_ventas(carrito, total):
    """
    Registra una venta exitosa en el historial general del sistema.

    Flujo principal:
        1. Recibe los datos del carrito y el total de la compra.
        2. Crea una entrada en el historial de ventas (`historial_ventas`) con:
            - Una copia del carrito actual (productos, precios y cantidades).
            - El monto total pagado.
        3. Muestra en consola una confirmación visual mediante `UT.cuadro_verde()`.

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
        - total (float): Valor total de la compra realizada.

    Dependencias:
        - UT (interfaz.utilidades): Para mostrar mensajes de confirmación con formato visual.

    Efectos:
        - Agrega una nueva entrada al registro global `historial_ventas`.
        - No retorna ningún valor.
        - Muestra en consola la notificación “Venta Registrada.”

    Ejemplo de registro generado:
        historial_ventas = [
            {
                "carrito": {
                    "pan": {"precio": 2000, "cantidad": 2},
                    "leche": {"precio": 3500, "cantidad": 1}
                },
                "total": 7500
            }
        ]
    """

    historial_ventas.append({"carrito": carrito.copy(), "total": total})
    UT.cuadro_verde("Venta Registrada.")

def generar_reportes(): 
    """
    Genera y guarda un reporte detallado de las ventas realizadas en el sistema.

    Flujo principal:
        1. Verifica si existen ventas registradas en `historial_ventas`.
            - Si no hay registros, muestra un mensaje de advertencia y detiene la ejecución.
        2. Recorre todas las ventas para:
            - Calcular el ingreso total acumulado.
            - Contar la cantidad total vendida de cada producto.
        3. Identifica el producto más vendido.
        4. Genera un resumen con:
            - Producto más vendido y unidades vendidas.
            - Total de compras registradas.
            - Total de ingresos generados.
        5. Crea un archivo `.txt` en la carpeta de reportes (`/Data/Reportes`) con esta información.
        6. Muestra el contenido del reporte en consola y confirma su guardado.

    Parámetros:
        - No recibe parámetros directamente.
        - Utiliza la variable global `historial_ventas`, que contiene todas las ventas registradas.

    Variables globales:
        - historial_ventas (list): Lista de ventas con estructura:
            [
                {
                    "carrito": {
                        "producto1": {"precio": float, "cantidad": int},
                        "producto2": {"precio": float, "cantidad": int}
                    },
                    "total": float
                },
                ...
            ]

    Dependencias:
        - collections.defaultdict: Para contar las unidades vendidas por producto.
        - datetime.datetime: Para generar un nombre de archivo con marca temporal.
        - os: Para manejar rutas y crear la carpeta de reportes.
        - UT (interfaz.utilidades): Para mostrar mensajes de color y formato en consola.

    Efectos:
        - Crea un archivo de texto con el resumen de ventas.
        - Muestra el contenido del reporte en consola.
        - Si no hay ventas, interrumpe el proceso y notifica al usuario.

    Ejemplo de contenido del reporte generado:
        ----- REPORTE DE VENTAS ----
        Producto más vendido: Pan (15 unidades)
        Número total de compras: 6
        Total de ingresos acumulados: $52,300.00
        ----------------------------

    Ruta de guardado por defecto:
        \Proyectos Prog\Python\PROYECTO TIENDA\MK-2.0\Sistem\Data\Reportes

    El nombre del archivo se genera automáticamente con el formato:
        reporte_YYYY_MM_DD__HH_MM_SS.txt
    """

    if not historial_ventas:
        UT.cuadro_rojo(" No hay ventas registradas.")
        return

    ventas_por_producto = defaultdict(int)
    ingresos_totales = 0

    for venta in historial_ventas:
        ingresos_totales += venta["total"]
        for producto, datos in venta["carrito"].items():
            ventas_por_producto[producto] += datos["cantidad"]

# Producto más vendido
    producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)

# Total de compras
    total_compras = len(historial_ventas)

    # Contenido del reporte
    contenido_reporte = '----- REPORTE DE VENTAS ----\n'
    contenido_reporte += f'Producto más vendido: {producto_mas_vendido} ({ventas_por_producto[producto_mas_vendido]} unidades)\n'
    contenido_reporte += f'Número total de compras: {total_compras}\n'
    contenido_reporte += f'Total de ingresos acumulados: ${ingresos_totales:.2f}\n'
    contenido_reporte += '----------------------------\n'



    # Ruta donde se guardan los recibos (ajusta si es necesario)
    ruta_relativa = r"..\MK-2.01\System\Data\Reportes" # Cambia dependiendo de donde este trabajando el proyecto (SI se deja en blanco el STR, SE GUARDA EN LA CARPETA RAIZ (Sistem))
    ruta_reportes = os.path.abspath(ruta_relativa) # Obtener ruta absoluta

    os.makedirs(ruta_reportes, exist_ok=True)

    # Parámetros de nombre del archivo
    tiempo = datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
    nombre_archivo = f"reporte_{tiempo}.txt"

    # Generar ruta completa del archivo
    ruta_archivo = os.path.join(ruta_reportes, nombre_archivo)

    # Guardar el recibo en un archivo de texto
    with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido_reporte)

    # Mostrar el recibo en consola y la confirmacion de guardado
    UT.cuadro_verde(contenido_reporte)
    UT.cuadro_verde(f'Reporte Generado: {ruta_archivo}')

