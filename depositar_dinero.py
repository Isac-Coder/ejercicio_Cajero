from ansi_colores import *
from tiempo_de_carga import cargar
from limpiar_pantalla import Limpiar_pantalla
from Validaciones import pedir_numero
from usuarios import *
from login import *



def depositar_dinero(usuario, CUENTAS):
        
        monto = pedir_numero(f"{VERDE}Ingrese el monto a depositar:{BLANCO}\n$ ")
        print(f"{VERDE}")
        Limpiar_pantalla()
        cargar()
        print("\n")
        Limpiar_pantalla()


        if monto <= 0:
            print(f"{ROJO}⚠️  El monto no puede ser un numero negativo o cero. ⚠️\n{VERDE}")
            print("Por favor, ingrese un monto válido.\n")
            input(f"{AMARILLO}Presione Enter para continuar...")

            Limpiar_pantalla()
            cargar()
            Limpiar_pantalla()
        else:
            if monto < 100:
                print(f"{ROJO}⚠️  El monto minimo permitido para depósito es de {BLANCO}$100.{ROJO} Intente nuevamente. ⚠️\n{VERDE}")
                input(f"{AMARILLO}Presione Enter para continuar...")

                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
                return
            CUENTAS[usuario]["saldo"] += monto
            print(f"✅ Depósito exitoso. Nuevo saldo:\n")
            print(f"{BLANCO}$ {int(CUENTAS[usuario]['saldo'])}{VERDE}\n")
            input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")

            Limpiar_pantalla()
            cargar()
            Limpiar_pantalla()

    