import time
import random
import os

# Colores de texto
NEGRO = "\u001b[30m"
ROJO = "\u001b[31m"
VERDE = "\u001b[32m"
AMARILLO = "\u001b[33m"
AZUL = "\u001b[34m"
MOSADO = "\u001b[35m"
CELESTE = "\u001b[36m"
BLANCO = "\u001b[37m"

# Colores de fondo
F_NEGRO = "\u001b[40m"
F_ROJO = "\u001b[41m"
F_VERDE = "\u001b[42m"
F_AMARILLO = "\u001b[43m"
F_AZUL = "\u001b[44m"
F_ROSADO = "\u001b[45m"
F_CELESTE = "\u001b[46m"
F_BLANCO = "\u001b[47m"

# Reset
RESET = "\u001b[0m"




historial_operaciones = []

def pedir_numero(mensaje, al_error=None):
    """
    Pide un número al usuario. Si al_error es una función, se llama tras
    entrada inválida (después de limpiar pantalla) para volver a mostrar el menú.
    """
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("\nEntrada inválida. Debe ingresar un número.")
            input(f"{AMARILLO}Presione ENTER para continuar\n")
            Limpiar_pantalla()
            if al_error:
                al_error()

def cargar():
    print(f"{VERDE}Cargando", end="")
    for _ in range(3):
        time.sleep(random.uniform(0.5, 1.5))
        print(".", end="", flush=True)

def Limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def registrar_operacion(descripcion):
    """
    Agrega una descripción de operación al historial.
    """
    historial_operaciones.append(descripcion)

def mostrar_historial():
    Limpiar_pantalla()
    cargar()
    Limpiar_pantalla()

    print(f"{AMARILLO}╔═══════════╗")
    print(f"║{VERDE} HISTORIAL {AMARILLO}║")
    print(f"╚═══════════╝{VERDE}\n")

    if not historial_operaciones:
        print(f"{ROJO} No hay operaciones en el historial.{VERDE}\n")
        input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()
    else:
        for i, operacion in enumerate(historial_operaciones, 1):
            print(f"║ {i}. {operacion}")
            print("╚════════════════════╝\n")
        input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()
