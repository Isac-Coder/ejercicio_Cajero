from colores import *
from limpiar_pantalla import Limpiar_pantalla
from main import saldo

while True:
    def depositar_dinero():
        Limpiar_pantalla()
        global saldo
        monto = float(input(f"{VERDE}Ingrese el monto a depositar:\n$ "))
        
        if monto <= 1000:
            print(f"{ROJO}⚠️  El monto debe ser mayor que 1000. ⚠️\n{VERDE}")
            print("Por favor, ingrese un monto válido.\n")
            input("Presione Enter para continuar...")
            Limpiar_pantalla()
        else:
            if monto < 1000:
                print(f"{ROJO}⚠️  El monto minimo permitido para depósito es de $1,000. Intente nuevamente. ⚠️\n{VERDE}")
                input("Presione Enter para continuar...")
                Limpiar_pantalla()
                return
            saldo += monto
            print(f"✅ Depósito exitoso. Nuevo saldo: ${int(saldo)}")
            input("Presione Enter para continuar...")
            Limpiar_pantalla()
    depositar_dinero()