from codigo.login import autenticar
from codigo.usuarios import CUENTAS
from codigo.MENU import menu
from codigo.bienvenida import bienvenida
from codigo.depositar_dinero import depositar_dinero
from codigo.Retirar import retirar_dinero
from codigo.saldo import consultar_saldo
from codigo.salir import salir
from codigo.crear_cuenta import crear_cuenta
from codigo.funciones import *

def main():
    Limpiar_pantalla()
    bienvenida()
    Limpiar_pantalla()

    # Pantalla: Iniciar sesión o Crear cuenta
    while True:
        Limpiar_pantalla()
        print(f"{VERDE}╔═══════════════════════════════╗")
        print(f"║{AMARILLO}   ¿Qué desea hacer?           {VERDE}║")
        print(f"╠═══════════════════════════════╣")
        print(f"║  1. Iniciar sesión            ║")
        print(f"║  2. Crear cuenta              ║")
        print(f"╚═══════════════════════════════╝{VERDE}\n")
        opcion_inicio = input(f"{AMARILLO}Seleccione una opción (1 o 2):{BLANCO} ").strip()
        if opcion_inicio == "2":
            crear_cuenta()
            continue
        if opcion_inicio == "1":
            break
        print(f"{ROJO}Opción inválida. Elija 1 o 2.{VERDE}")
        input(f"{AMARILLO}Presione ENTER para continuar...{VERDE}")

    usuario = autenticar()
    Limpiar_pantalla()
    

    while True:
        if usuario is None:
            print("🔒 Sistema bloqueado.")
            exit()
        menu()
        # Leer opción del menú validando que sea numérica
        opcion = int(pedir_numero(f"selecciona una opcion:{BLANCO}\n# ", al_error=menu))

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