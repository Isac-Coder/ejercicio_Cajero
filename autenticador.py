from usuarios import CUENTAS

MAX_INTENTOS = 3

def autenticar():
    intentos = 0

    while intentos < MAX_INTENTOS:
        print("Ingrese su usuario: ")
        usuario = input().strip()

        if usuario not in CUENTAS:
            print("Usuario incorrecto")
            intentos += 1
            print(f"Intentos restantes {MAX_INTENTOS - intentos}")
            continue

        while True:
            print("Ingrese su PIN de 4 numeros: ")
            pin_ingresado = input().strip()

            if not pin_ingresado.isdigit():
                print("El PIN debe contener solo numeros")
                continue

            if CUENTAS[usuario]["clave"] == pin_ingresado:
                print("Autenticacion exitosa")
                return usuario
            else:
                print("PIN incorrecto")
                intentos += 1
                print(f"Intentos restantes {MAX_INTENTOS - intentos}")
                break

    print("Cuenta suspendida temporalmente por demasiados intentos")
    return None

autenticar()