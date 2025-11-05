
#----IMPORTACIONES DE MODULOS NECESARIOS----
try:    
    from functions import ValidacionesTrabajadores as VTS, MenuCompra as MC
    from utils import interfazMain as IM, utilidades as UT
    import sys
    import time
    from functions import inicioSesion as INSS
except ImportError as e:
    print(f"Error al importar módulos: {e}")
    raise

#----FUNCION PRINCIPAL DEL PROGRAMA----
def main():
    """
    Función principal del sistema de tienda.

    Controla el flujo principal del programa y presenta el menú inicial de interacción
    con el usuario. Permite acceder a las opciones de compra y a las funciones exclusivas 
    para trabajadores (como inicio de sesión y registro de nuevos usuarios).

    Flujo general:
        1. Muestra el banner principal del sistema.
        2. Despliega el menú principal con tres opciones:
            - Comprar un producto.
            - Opción para trabajadores.
            - Salir del programa.
        3. Gestiona la selección del usuario mediante una estructura 'match case':
            - Opción 1: Redirige al módulo de compra (MC.menucompra()).
            - Opción 2: Muestra un submenú para trabajadores con opciones de inicio
              de sesión, registro y retorno al menú principal.
            - Opción 3: Finaliza el programa mostrando un mensaje de salida.

    Este bucle principal se repite indefinidamente hasta que el usuario elige salir.
    
    """

    
#menu inicio de sesion
    while True:
        IM.banner() #imprime el banner del programa en consola
        UT.cuadro_cyan("BIENVENIDO, POR FAVOR INCIE SESION")
        if INSS.inicio_sesion_main():

            # Menú de interacción
            while True: 
                
                IM.banner() #imprime el banner del programa en consola


                UT.cuadro_naranja("""--- MENÚ PRINCIPAL ---

        1. Comprar un producto 
        2. Opcion para Trabajadores
        3. Salir 
        """) #Menu principal
                seleccion = input("Ingrese un número: ") #El Usuario selecciona lo que aparece en el menu principal

        #validacion de seleccion del usuario
                match seleccion:
                    case "1":
                        UT.clear()
                        MC.menucompra()

                    case "2":
                        while True:
                            UT.clear()
                            UT.cuadro_naranja("""---BIENVENIDO---

        1. Iniciar sesión
        2. Registrar nuevo usuario
        3. Volver al menú principal
        """)
                            
                            opcion_trabajador = input("Seleccione una opción: ")
                            match opcion_trabajador:
                                case "1": #Iniciar sesión, si es verdadero entra al menu de trabajador
                                    UT.clear()
                                    if VTS.login():
                                        VTS.opciones_trabajador()
                                    time.sleep(1)
                                    break
                                case "2": #Registrar nuevo usuario
                                    UT.clear()
                                    VTS.registrar_usuario()
                                    time.sleep(1)
                                case "3":
                                    UT.cuadro_rojo("Volviendo al menú principal... ")
                                    time.sleep(1)
                                    break
                                case _:
                                    UT.cuadro_rojo(" Opción no válida, por favor intente nuevamente.")
                                    time.sleep(1)


                    case"3":
                        red = "\033[91m"
                        reset = "\033[0m"
                        UT.clear()
                        UT.cuadro_verde(" Finalizando programa... ")
                        print(red +r"                       MK-2.0")
                        print(r"                     By: AyLz "+ reset )
                        time.sleep(1.2)
                        sys.exit()
                    case _:
                        UT.cuadro_rojo(" Opción no válida, por favor intente nuevamente.")

#Arranque del programa
if __name__ == "__main__":
    main()