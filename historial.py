from colores import *
from tiempo_de_carga import cargar
from limpiar_pantalla import Limpiar_pantalla

historial = []

def historial():
    Limpiar_pantalla()
    cargar()
    print("\n")
    if not historial:
            print(f"{ROJO}No hay operaciones en el historial.{VERDE}\n")
    else:
        cargar()
        print("\n")
        Limpiar_pantalla()
        print(f"{AMARILLO}┌───────────┐")
        print("│ HISTORIAL │")
        print("└───────────┘\n")
        print(f" =======================================")
        for i, operacion in enumerate(historial, 1):
            print(f"| {i}. {operacion}")
        print(" =======================================\n")

historial()