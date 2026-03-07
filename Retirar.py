from funciones import *
from login import *
from datetime import date


LIMITE_DIARIO_RETIRO = 1_000_000


def retirar_dinero(usuario, CUENTAS):
    Limpiar_pantalla()
    cargar()
    Limpiar_pantalla()

    cuenta = CUENTAS[usuario]
    hoy = date.today().isoformat()

    # Reiniciar acumulado diario si es un nuevo día
    if cuenta.get("fecha_ultimo_retiro") != hoy:
        cuenta["fecha_ultimo_retiro"] = hoy
        cuenta["retirado_hoy"] = 0

    retirado_hoy = cuenta.get("retirado_hoy", 0)

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

    elif retirar > cuenta["saldo"]:
        print(f"{ROJO}No se puede retirar más del saldo disponible.\n")
        input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()

    elif retirado_hoy + retirar > LIMITE_DIARIO_RETIRO:
        restante = LIMITE_DIARIO_RETIRO - retirado_hoy
        print(
            f"{ROJO}Límite diario de retiro excedido.\n"
            f"Solo puede retirar {BLANCO}$ {int(restante)}{ROJO} más hoy.{VERDE}\n"
        )
        input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()

    else:
        cuenta["saldo"] -= retirar
        cuenta["retirado_hoy"] = retirado_hoy + retirar
        saldo_restante = int(cuenta["saldo"])

        registrar_operacion(
            f"Retiro de $ {int(retirar)}. Nuevo saldo: $ {saldo_restante}"
        )
        print(f"{VERDE}Retiro exitoso.\n")
        print(f"Usted retiró:{BLANCO} $ {int(retirar)}{VERDE}\n")
        print(
            f"{VERDE}Saldo restante en su cuenta:{BLANCO} $ {saldo_restante}{VERDE}\n"
        )
        input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()