from ansi_colores import *
from tiempo_de_carga import cargar
from limpiar_pantalla import Limpiar_pantalla

historial_operaciones = []

def mostrar_historial():
    Limpiar_pantalla()
    cargar()
    Limpiar_pantalla()

    print(f"{AMARILLO}┌───────────┐")
    print(f"│{VERDE} HISTORIAL {AMARILLO}│")
    print(f"└───────────┘{VERDE}\n")

    if not historial_operaciones:
        print(f"{ROJO} No hay operaciones en el historial.{VERDE}\n")
        input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()
    else:
        for i, operacion in enumerate(historial_operaciones, 1):
            print(f"│ {i}. {operacion}")
            print("└────────────────────┘\n")

mostrar_historial()