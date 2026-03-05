from colores import *
from limpiar_pantalla import Limpiar_pantalla

def bienvenida():
    Limpiar_pantalla()
    print(f"{VERDE}")
    print("┌───────────────────────────────┐")
    print(f"│{AMARILLO}Bienvenido Al Cajero Automatico{VERDE}│")
    print(f"└───────────────────────────────┘\n{VERDE}")
    print("┌───────────────────────────────┐")
    print(f"│{AMARILLO}     Seleccione una opción     {VERDE}│")
    print("├───────────────────────────────┤")
    print("│  1. Retirar Dinero.           │")
    print("│  2. Depositar Dinero          │")
    print("│  3. Consultar Saldo           │")
    print(f"│{ROJO}  4. Salir{VERDE}                     │")
    print("└───────────────────────────────┘\n")
    

bienvenida()