#Menu
from ansi_colores import *
from limpiar_pantalla import Limpiar_pantalla
from tiempo_de_carga import cargar


def salir():
    Limpiar_pantalla()
    cargar()
    Limpiar_pantalla()
    print(f"{VERDE}Gracias por usar el cajero automático ")
    input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
    Limpiar_pantalla()
    exit()
    

