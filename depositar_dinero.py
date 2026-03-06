from ansi_colores import *
from tiempo_de_carga import cargar
from limpiar_pantalla import Limpiar_pantalla
from Validaciones import pedir_numero
from usuarios import CUENTAS
from login import *



def depositar_dinero(usuarios, CUENTAS):
        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()
        print("\n")
        monto_deposito = pedir_numero(f"{VERDE}Ingrese el monto a depositar:{BLANCO}\n$ ")
        print(f"{VERDE}")
        Limpiar_pantalla()
        cargar()
        print("\n")
        Limpiar_pantalla()


        if monto_deposito <= 0:
            print(f"{ROJO}⚠️  El monto no puede ser un numero negativo o cero. ⚠️\n{VERDE}")
            print("Por favor, ingrese un monto válido.\n")
            input(f"{AMARILLO}Presione Enter para continuar...")

            Limpiar_pantalla()
            cargar()
            Limpiar_pantalla()
        else:
            if monto_deposito < 100:
                print(f"{ROJO}⚠️  El monto minimo permitido para depósito es de {BLANCO}$100.{ROJO} Intente nuevamente. ⚠️\n{VERDE}")
                input(f"{AMARILLO}Presione Enter para continuar...")

                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
                return
"""            CUENTAS[usuario]["saldo"] += monto_deposito
            print(f"✅ Depósito exitoso. Nuevo saldo:\n")
            print(f"{BLANCO}$ {int(CUENTAS[usuario]['saldo'])}{VERDE}\n")
            input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
"""
        if usuario in CUENTAS["usuarios"]:

            if "saldo" not in CUENTAS["usuarios"][usuario]:
                CUENTAS["usuarios"][usuario]["saldo"] = 0

            CUENTAS["usuarios"][usuario]["saldo"] += monto_deposito

            print(f"✅ Depósito exitoso. Nuevo saldo:\n")
            print(f"{BLANCO}$ {int(CUENTAS['usuarios'][usuario]['saldo'])}{VERDE}\n")

            input(f"{AMARILLO}Presione Enter para continuar...")

        else:
            print(f"{ROJO}El usuario no existe.{BLANCO}")

depositar_dinero("usuario", CUENTAS)