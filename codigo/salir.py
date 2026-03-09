#Menu
from codigo.funciones import *


def salir():
    Limpiar_pantalla()
    saliendo()
    Limpiar_pantalla()
    print(f"{VERDE}Gracias por usar el cajero automático ")
    input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
    Limpiar_pantalla()
    exit()
    

