from usuarios import CUENTAS

MAX_INTENTOS = 3

def autenticar():
    intentos = 0

    while intentos < MAX_INTENTOS:

        usuario = input("Ingrese su usuario: ").strip()

        if usuario not in CUENTAS:
            intentos += 1
            print("❌ Usuario incorrecto")
            print(f"Intentos restantes: {MAX_INTENTOS - intentos}")
            continue

        pin = input("Ingrese su PIN de 4 números: ").strip() and len(pin) == 4

        if not pin.isdigit() or len(pin) != 4:
            print("⚠ El PIN debe tener exactamente 4 números")
            continue

        if CUENTAS[usuario]["clave"] == pin:
            print("✅ Autenticación exitosa")
            return usuario

        intentos += 1
        print("❌ PIN incorrecto")
        print(f"Intentos restantes: {MAX_INTENTOS - intentos}")

    print("⛔ Cuenta suspendida temporalmente por demasiados intentos")
    return None