from colores import *
from tiempo_de_carga import cargar
from limpiar_pantalla import Limpiar_pantalla
from main import saldo

while True:
    def depositar_dinero():
        Limpiar_pantalla()
        global saldo
        monto = float(input(f"{VERDE}Ingrese el monto a depositar:{BLANCO}\n$ "))
        print(f"{VERDE}")

        Limpiar_pantalla()
        cargar()
        print("\n")
        Limpiar_pantalla()

        if monto != int:
                print(f"{ROJO}⚠️  El monto ingresado no es un número válido. Por favor, ingrese un monto numérico. ⚠️\n{VERDE}")
                input(f"{AMARILLO}Presione Enter para continuar...")
    
                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
                return
        elif monto <= 0:
            print(f"{ROJO}⚠️  El monto no puede ser un numero negativo o cero. ⚠️\n{VERDE}")
            print("Por favor, ingrese un monto válido.\n")
            input(f"{AMARILLO}Presione Enter para continuar...")

            Limpiar_pantalla()
            cargar()
            Limpiar_pantalla()
        else:
            if monto < 1000:
                print(f"{ROJO}⚠️  El monto minimo permitido para depósito es de {BLANCO}$1,000.{ROJO} Intente nuevamente. ⚠️\n{VERDE}")
                input(f"{AMARILLO}Presione Enter para continuar...")

                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
                return
            saldo += monto
            print(f"✅ Depósito exitoso. Nuevo saldo:\n")
            print(f"{BLANCO}$ {int(saldo)}{VERDE}\n")
            input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")

            Limpiar_pantalla()
            cargar()
            Limpiar_pantalla()
    depositar_dinero()