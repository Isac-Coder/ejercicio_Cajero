from login import autenticar
from usuarios import CUENTAS
from MENU import bienvenida
from depositar_dinero import depositar_dinero
from Retirar import retirar_dinero
from saldo import consultar_saldo
from salir import salir
from funciones import *


def main():
    Limpiar_pantalla()
    usuario = autenticar()
    Limpiar_pantalla()
    

    while True:
        if usuario is None:
             print("🔒 Sistema bloqueado.")
             exit()
        bienvenida()
        # Leer opción del menú validando que sea numérica
        opcion = int(pedir_numero(f"selecciona una opcion:{BLANCO}\n# ", al_error=bienvenida))

        if opcion == 2:
                depositar_dinero(usuario, CUENTAS)

        elif opcion == 1:
               retirar_dinero(usuario , CUENTAS)

        elif opcion == 3:
                consultar_saldo(usuario, CUENTAS)

        elif opcion == 4:
            mostrar_historial() 
        
        elif opcion == 5:
            salir()


        else:
            print(f"{ROJO}Opción inválida.{VERDE}")
            input(f"{AMARILLO}Presione ENTER para continuar\n")
            Limpiar_pantalla()

main()