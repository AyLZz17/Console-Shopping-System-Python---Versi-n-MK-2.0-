try:
    
    from Data import DatosTarjetasPago as DT
    from utils import utilidades as UT

except ImportError as e:
    print(f"Error al importar módulos: {e}")
    raise


def procesar_pago(total, tarjeta):
    """
    Procesa el pago de una compra verificando la existencia de la tarjeta y el saldo disponible.

    Flujo del proceso:
        1. Recorre el diccionario `DT.tarjetas`, que contiene todas las tarjetas registradas en el sistema.
        2. Busca una coincidencia entre el número de tarjeta ingresado por el usuario (`tarjeta`) y los valores en el diccionario.
        3. Si encuentra la tarjeta:
            - Comprueba si el saldo disponible (`t["saldo"]`) es mayor o igual al monto total de la compra (`total`).
            - Si hay saldo suficiente:
                - Resta el valor del total al saldo de la tarjeta.
                - Muestra un mensaje verde confirmando el pago y mostrando el saldo restante.
                - Retorna `True` indicando que el pago fue exitoso.
            - Si no hay saldo suficiente:
                - Muestra un recuadro rojo indicando “saldo insuficiente”.
                - Retorna `False`.
        4. Si no se encuentra ninguna tarjeta con el número ingresado:
            - Muestra un recuadro rojo indicando que la tarjeta no fue encontrada.
            - Retorna `False`.

    Parámetros:
        total (float): Monto total a pagar.
        tarjeta (str): Número de tarjeta ingresado por el usuario.

    Retorna:
        bool: 
            - `True` si el pago se realiza correctamente.
            - `False` si la tarjeta no existe o el saldo es insuficiente.

    Efectos:
        - Modifica el saldo en el diccionario `DT.tarjetas` si el pago es exitoso.
        - Muestra mensajes en consola usando las funciones de interfaz `UT`.

    Dependencias:
        - `DT` (DatosTarjetasPago): contiene el diccionario `tarjetas` con los datos de las tarjetas.
        - `UT` (interfaz.utilidades): para mostrar los recuadros de mensaje y formato visual.

    Excepciones:
        - No lanza errores. Todas las validaciones se manejan con mensajes controlados.
    """
    for t in DT.tarjetas.values(): #recorre el diccionario de tarjetas localizado en DatosTarjetasPago.py
        if t["numero"] == tarjeta: #validaciones
            if t["saldo"] >= total:
                t["saldo"] -= total
                UT.cuadro_verde(f" Pago realizado con éxito.\n Saldo restante: ${t['saldo']:.2f}")
                
                return True #si el pago es realizado, muestra en pantalla la confirmación y hace una limpieza al carrito y retorna verdadero 
            
            else:
                UT.cuadro_rojo(" Pago rechazado: saldo insuficiente.")
                return False #si no hay saldo suficiente, muestra el error y retorna falso

    # Si no encontró la tarjeta
    UT.cuadro_rojo(" Pago rechazado: tarjeta no encontrada.")
    return False #si la tarjeta no existe, muestra el error y retorna falso
