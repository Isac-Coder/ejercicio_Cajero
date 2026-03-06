from funciones import *

def menu():
    Limpiar_pantalla()
    print(f"{VERDE}")
    print("╔═══════════════════════════════╗")
    print(f"║{AMARILLO}Bienvenido Al Cajero Automatico{VERDE}║")
    print(f"╚═══════════════════════════════╝{VERDE}")
    print("╔═══════════════════════════════╗")
    print(f"║{AMARILLO}     Seleccione una opción     {VERDE}║")
    print("╠═══════════════════════════════╣")
    print("║  1. Retirar Dinero.           ║")
    print("║  2. Depositar Dinero          ║")
    print("║  3. Consultar Saldo           ║")
    print("║  4. Consultar Historial       ║")
    print(f"║{ROJO}  5. Salir{VERDE}                     ║")
    print("╚═══════════════════════════════╝\n")
