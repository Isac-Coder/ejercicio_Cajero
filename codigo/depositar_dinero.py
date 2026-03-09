from codigo.funciones import *
from codigo.usuarios import CUENTAS
from codigo.login import *


LIMITE_MAX_DEPOSITO = 1_000_000


def depositar_dinero(usuario, CUENTAS):
    Limpiar_pantalla()
    cargar()
    Limpiar_pantalla()
    print("\n")
    monto_deposito = pedir_numero(
        f"{VERDE}Ingrese el monto a depositar:{BLANCO}\n$ "
    )
    print(f"{VERDE}")
    Limpiar_pantalla()
    cargar()
    print("\n")
    Limpiar_pantalla()

    # Validaciones de monto
    if monto_deposito <= 0:
        print(
            f"{ROJO}⚠️  El monto no puede ser un numero negativo o cero. ⚠️\n{VERDE}"
        )
        print("Por favor, ingrese un monto válido.\n")
        input(f"{AMARILLO}Presione Enter para continuar...")

        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()
        return
    elif monto_deposito < 100:
        print(
            f"{ROJO}⚠️  El monto minimo permitido para depósito es de {BLANCO}$100.{ROJO} Intente nuevamente. ⚠️\n{VERDE}"
        )
        input(f"{AMARILLO}Presione Enter para continuar...")

        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()
        return
    elif monto_deposito > LIMITE_MAX_DEPOSITO:
        print(
            f"{ROJO}⚠️  El monto máximo permitido para depósito es de {BLANCO}$ {int(LIMITE_MAX_DEPOSITO)}.{ROJO} Intente nuevamente. ⚠️\n{VERDE}"
        )
        input(f"{AMARILLO}Presione Enter para continuar...")

        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()
        return

    # Actualización de saldo
    if usuario in CUENTAS:
        if "saldo" not in CUENTAS[usuario]:
            CUENTAS[usuario]["saldo"] = 0

        CUENTAS[usuario]["saldo"] += monto_deposito

        registrar_operacion(
            f"Depósito de $ {int(monto_deposito)}. Nuevo saldo: $ {int(CUENTAS[usuario]['saldo'])}"
        )

        print(f"✅ Depósito exitoso. Nuevo saldo:\n")
        print(f"{BLANCO}$ {int(CUENTAS[usuario]['saldo'])}{VERDE}\n")

        input(f"{AMARILLO}Presione Enter para continuar...")
    else:
        print(f"{ROJO}El usuario no existe.{BLANCO}")