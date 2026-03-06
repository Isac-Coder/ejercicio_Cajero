from login import autenticar
from usuarios import CUENTAS
from MENU import bienvenida
from depositar_dinero import depositar_dinero
from Retirar import retirar_dinero
from saldo import consultar_saldo
from Boton_salir import salir
from limpiar_pantalla import *

def main():
    Limpiar_pantalla()
    usuario = autenticar()
    Limpiar_pantalla()
    

    while True:
        bienvenida()


        opcion =  int(input("selecciona una opcion\n"))     # mostrar menu

        if opcion == 2:
                depositar_dinero(usuario, CUENTAS)

        elif opcion == 1:
               retirar_dinero(usuario , CUENTAS)

        elif opcion == 3:
                consultar_saldo()

        elif opcion == 4:
            (salir)


        else:
            print("Opción inválida")

main()