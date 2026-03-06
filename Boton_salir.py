#Menu
from funciones import *


def salir():
    Limpiar_pantalla()
    cargar()
    Limpiar_pantalla()
    print(f"{VERDE}Gracias por usar el cajero automático ")
    input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
    Limpiar_pantalla()
    exit()
    

