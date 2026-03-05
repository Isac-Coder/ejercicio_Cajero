from colores import *
from tiempo_de_carga import cargar
from limpiar_pantalla import Limpiar_pantalla

def pedir_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print(f"{ROJO}Entrada inválida. Debe ingresar un número.")
            input(f"{AMARILLO}Presione Enter para continuar...")
            Limpiar_pantalla()
            cargar()
            Limpiar_pantalla()