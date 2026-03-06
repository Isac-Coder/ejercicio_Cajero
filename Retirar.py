#Consultar saldo

from Validaciones import pedir_numero
from ansi_colores import *
from limpiar_pantalla import Limpiar_pantalla
from tiempo_de_carga import cargar
from login import *
from Historial import registrar_operacion
    
def retirar_dinero(usuario, CUENTAS):
    Limpiar_pantalla()
    cargar()
    Limpiar_pantalla()
    retirar = pedir_numero(f"{VERDE}Ingrese el valor que desea retirar:{BLANCO}\n$ ")
    Limpiar_pantalla()
    cargar()
    Limpiar_pantalla()

    if retirar <= 0:
        print(f"{ROJO}No se permiten montos negativos o cero.\n")
        input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()

    elif retirar > CUENTAS[usuario]["saldo"]:
        print(f"{ROJO}No se puede retirar más del saldo disponible.\n")
        input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()

    else:
        CUENTAS[usuario]["saldo"] -= retirar
        registrar_operacion(
            f"Retiro de $ {int(retirar)}. Nuevo saldo: $ {int(CUENTAS[usuario]['saldo'])}"
        )
        print(f"{VERDE}Retiro exitoso.\n")
        print("Su nuevo saldo es:", int(CUENTAS[usuario]["saldo"]),"\n")
        input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()