"""
Módulo para crear una nueva cuenta y guardarla en el diccionario (persistido en JSON).
"""
import usuarios
from funciones import *


def crear_cuenta():
    """Pide usuario, PIN y saldo inicial; valida y agrega la cuenta al diccionario y al JSON."""
    Limpiar_pantalla()
    print(f"{VERDE}╔═══════════════════════════════╗")
    print(f"║{AMARILLO}       CREAR NUEVA CUENTA       {VERDE}║")
    print(f"╚═══════════════════════════════╝{VERDE}\n")

    # Usuario: solo letras, único
    while True:
        usuario = input(f"{VERDE}👤 Ingrese nombre de usuario (solo letras):{BLANCO} ").lower().strip()
        if not usuario:
            print(f"{ROJO}El usuario no puede estar vacío.{VERDE}\n")
            continue
        if not usuario.isalpha():
            print(f"{ROJO}Solo se permiten letras en el usuario.{VERDE}\n")
            continue
        if usuario in usuarios.CUENTAS:
            print(f"{ROJO}Ese usuario ya existe. Elija otro.{VERDE}\n")
            continue
        break

    # PIN de 4 dígitos con confirmación
    while True:
        pin = input(f"{VERDE}🔒 Ingrese PIN de 4 números:{BLANCO} ").strip()
        if not pin.isdigit():
            print(f"{ROJO}El PIN solo puede contener números.{VERDE}\n")
            continue
        if len(pin) != 4:
            print(f"{ROJO}El PIN debe tener exactamente 4 dígitos.{VERDE}\n")
            continue
        pin_confirmar = input(f"{VERDE}🔒 Confirme su PIN:{BLANCO} ").strip()
        if pin != pin_confirmar:
            print(f"{ROJO}Los PIN no coinciden. Intente de nuevo.{VERDE}\n")
            continue
        break

    # Saldo inicial
    saldo_inicial = 1000
    while True:
        saldo_texto = input(f"{VERDE}💰 Saldo inicial (Enter = 1000):{BLANCO} ").strip()
        if not saldo_texto:
            break
        try:
            saldo_inicial = float(saldo_texto)
            if saldo_inicial < 0:
                print(f"{ROJO}El saldo no puede ser negativo.{VERDE}\n")
                continue
            break
        except ValueError:
            print(f"{ROJO}Ingrese un número válido.{VERDE}\n")

    # Añadir al diccionario y guardar en JSON
    usuarios.CUENTAS[usuario] = {
        "clave": pin,
        "saldo": saldo_inicial,
    }
    usuarios.guardar_cuentas()

    print(f"\n{VERDE}✅ Cuenta creada correctamente para '{usuario}'.{VERDE}")
    input(f"{AMARILLO}Presione ENTER para continuar...{VERDE}")
    Limpiar_pantalla()
