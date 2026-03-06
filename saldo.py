from Validaciones import pedir_numero
from usuarios import CUENTAS

def consultar_saldo(usuario, CUENTAS):
    print("Su saldo actual es", CUENTAS[usuario]["saldo"] )

