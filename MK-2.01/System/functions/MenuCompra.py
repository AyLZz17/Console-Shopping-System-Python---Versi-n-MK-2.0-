try:   
    from functions import reportes as rep, RecibosVenta as RV, ValidacionesTrabajadores as VTS, GestionProductos as GDP, mainPagos as SPG
    from utils import utilidades as UT

except ImportError as e:
    print(f"Error al importar módulos: {e}")
    raise



carrito = {} #Almacenamiento del Carrito de compras
total = 0 # Variable inicial del total a pagar

def mostrar_carrito():
    """
    Muestra en consola el contenido actual del carrito de compras con su detalle y total a pagar.

    Flujo del proceso:
        1. Limpia la consola utilizando `UT.clear()`.
        2. Inicializa una variable `menu_carrito` con el encabezado principal del carrito.
        3. Verifica si el carrito está vacío:
            - Si está vacío, muestra un recuadro rojo indicando que no hay productos.
        4. Si hay productos en el carrito:
            - Recorre cada producto contenido en el diccionario `carrito`.
            - Calcula el subtotal multiplicando precio por cantidad.
            - Añade al texto de la interfaz una línea con el nombre, cantidad, precio y subtotal.
            - Suma cada subtotal al total general.
        5. Al final, añade a la interfaz el total de productos y el monto total a pagar.
        6. Muestra todo el contenido del carrito en un recuadro naranja usando `UT.cuadro_naranja()`.

    Variables globales:
        - `carrito` (dict): Contiene los productos añadidos con sus precios y cantidades.
        - `total` (float): Acumula el monto total a pagar por los productos del carrito.

    Parámetros:
        Ninguno.

    Retorna:
        None

    Efectos:
        - Imprime en consola el contenido del carrito y su total.
        - Actualiza el valor global de `total`.

    Ejemplo de salida:
        ===============TU CARRITO===============
        - Pan: 2 x $1.50 = $3.00
        - Leche: 1 x $2.00 = $2.00
        Total de productos: 2 |  Total a pagar: $5.00
        ==========================
    """
    UT.clear() #Limpia la colsola

    menu_carrito = "===============TU CARRITO===============\n" #variable inicial de la interfaz del carrito

    if not carrito: #validacion si el carrito tiene o no items
        UT.cuadro_rojo("El carrito está vacío.")
    else:
        global total
        total = 0 #variable inicial para pagos
        for nombre, datos in carrito.items(): #recorre los items del carrito y los imprime en consola
            subtotal = datos['precio'] * datos['cantidad']
            menu_carrito += f"- {nombre.title()}: {datos['cantidad']} x ${datos['precio']} = ${subtotal:.2f}\n" #añade item por item a la variable de interfaz del carrito
            total += subtotal
        menu_carrito += f" Total de productos: {len(carrito)} |  Total a pagar: ${total:.2f}" #añade a la interfaz del carritov el texto del total de productos y total al pagar
        UT.cuadro_naranja(menu_carrito) #imprime la interfaz del carrito completa


    print("==========================\n")

def menucompra():

    """
    Inicia y gestiona el proceso completo de compra de productos por parte del cliente.

    Flujo principal:
        1. Muestra todos los productos disponibles con su precio y cantidad en stock.
        2. Permite al usuario:
            - Seleccionar un producto para añadir al carrito.
            - Escribir 'carrito' para revisar, pagar o vaciar el carrito.
            - Escribir 'salir' para finalizar el proceso de compra.
        3. Al seleccionar un producto:
            - Solicita la cantidad deseada.
            - Valida que sea un número entero mayor a cero.
            - Verifica disponibilidad en el inventario.
            - Si hay stock suficiente, añade el producto al carrito y descuenta del inventario.
        4. En el menú del carrito:
            - 'p': Procesa el pago solicitando el número de tarjeta.
                - Si el pago es exitoso:
                    - Registra la venta en el historial (`rep.registrar_ventas()`).
                    - Genera un recibo (`RV.generar_recibo()`).
                    - Guarda los cambios en el inventario (`GDP.guardar_productos()`).
                    - Limpia el carrito.
                - Si el pago falla, muestra el error correspondiente.
            - 'v': Vacía el carrito.
            - Enter: Vuelve al menú de productos.
        5. Al escribir 'salir', termina el proceso y retorna al menú principal.

    Variables globales:
        - carrito (dict): Contiene los productos añadidos, con su precio y cantidad.
        - total (float): Acumula el valor total de los productos en el carrito.

    Dependencias:
        - UT (interfaz.utilidades): Para imprimir recuadros y limpiar la consola.
        - GDP (GestionProductos): Para acceder al inventario y guardar cambios.
        - SPG (mainPagos): Para procesar pagos mediante tarjetas.
        - rep (reportes): Para registrar las ventas realizadas.
        - RV (RecibosVenta): Para generar recibos de compra.

    Efectos:
        - Modifica el inventario de productos (`GDP.productos`).
        - Puede registrar ventas y generar recibos.
        - Interactúa con el usuario por consola en tiempo real.

    Ejemplo de flujo de uso:
        - Usuario ingresa “pan” → selecciona cantidad → se añade al carrito.
        - Usuario ingresa “carrito” → ve total → selecciona “p” → ingresa tarjeta → pago exitoso.
        - Se genera recibo, se actualiza inventario y se limpia el carrito.
    """

#bucle principal del menu de compras
    while True:
        UT.clear() #limpia consola
        menu_texto = "=== MENÚ DE PRODUCTOS DISPONIBLES ===\n" #inicializa la variable de la interfaz del menu de productos disponibles
        for nombre, datos in GDP.productos.items(): #recorre el diccionario de productos y los imprime en consola
            menu_texto += f"- {nombre.title()}: Precio ${datos['precio']}, Cantidad disponible: {datos['cantidad']}\n"
        menu_texto += "=================================================================================\n"
        menu_texto += "Escriba 'carrito' para ver o pagar su carrito, o 'salir' para terminar la compra."

        UT.cuadro_naranja(menu_texto) #imprime la interfaz de productos disponibles

        opcion = input("Por favor, ingrese una opción: ").lower() #el usuario ingresa su opcion de compra

        if opcion == 'carrito':#validacion de la opcion del usuario
            UT.clear()
            mostrar_carrito() #muestra el carrito 
            if carrito:
                accion = input("¿Desea pagar (p), vaciar (v) o volver (enter)? ").lower() #seleccion del usuario
                if accion == 'p':#validacion de la opcion del usuario
                    UT.clear()
                    UT.cuadro_naranja("=== CARRITO DE COMPRAS ===") 
                    UT.cuadro_cyan(f" Su total es: ${total:.2f}")

                    tarjeta = input("Ingrese el número de tarjeta: ")
                    if SPG.procesar_pago(total, tarjeta) == True:  # EJECUTA EL PROCESO DE PAGOS Y VERIFICA SI FUE EXITOSO
                        rep.registrar_ventas(carrito, total)  # registra la venta en el historial
                        RV.generar_recibo(carrito, total)  # Llama a la función para generar el recibo
                        GDP.guardar_productos(GDP.productos)  # guarda los cambios en el inventario
                        input("Presione Enter para continuar...")  
                        carrito.clear()
                    break
                elif accion == 'v':
                    carrito.clear()
                    UT.cuadro_rojo(" Carrito vaciado correctamente.")
                continue
        elif opcion == 'salir':
                UT.cuadro_rojo(" Saliendo del menú de compras.")
                break

        elif opcion in GDP.productos: #validacion si la opcion esta en los productos disponibles
            menu_opcion = f"PRODUCTO: {opcion.title()}. PRECIO: ${GDP.productos[opcion]['precio']}. CANTIDAD: {GDP.productos[opcion]['cantidad']}."
            UT.cuadro_cyan(menu_opcion) #imprime el producto seleccionado con sus carateristicas
            try: #Encarga de añadir cuantos itenms del objeto que quiere el usuario
                cantidadBuy = int(input("Ingrese la cantidad que desea comprar (Solo números Enteros): "))
            except ValueError: #si seleciona un numero FLOAT o algun caracter arroja error e impide que el programa crashee
                UT.cuadro_rojo(" Por favor, ingrese un número válido.")
                continue

            if cantidadBuy <= 0: #validaciones
                UT.cuadro_rojo(" La cantidad debe ser mayor a cero.")
                continue

            if cantidadBuy <= GDP.productos[opcion]["cantidad"]: #validaciones
                if opcion in carrito: #validaciones
                    carrito[opcion]['cantidad'] += cantidadBuy
                else: #validaciones
                    carrito[opcion] = {
                        'precio': GDP.productos[opcion]['precio'],
                        'cantidad': cantidadBuy
                    }
                GDP.productos[opcion]["cantidad"] -= cantidadBuy
                UT.cuadro_verde(f" {cantidadBuy} {opcion}(s) añadido(s) al carrito ")
            else: #validaciones
                UT.cuadro_rojo(
                    f" Lo siento, no hay suficiente cantidad de {opcion}.\n"
                    f"Cantidad disponible: {GDP.productos[opcion]['cantidad']}"
                )
        else: 
            UT.cuadro_rojo(" Selección invalida. Intente de nuevo.")


