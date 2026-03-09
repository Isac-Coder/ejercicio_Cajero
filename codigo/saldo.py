from codigo.funciones import *
from codigo.usuarios import CUENTAS


def consultar_saldo(usuario, CUENTAS):
    Limpiar_pantalla()
    cargar()
    Limpiar_pantalla()
    saldo_actual = int(CUENTAS[usuario]["saldo"])
    print(f"Su saldo actual es: {BLANCO}$ {saldo_actual}{VERDE}")
    registrar_operacion(f"Consulta de saldo. Saldo actual: $ {saldo_actual}")
    input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
    Limpiar_pantalla()
    cargar()
    Limpiar_pantalla()