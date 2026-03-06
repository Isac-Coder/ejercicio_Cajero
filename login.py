from usuarios import CUENTAS
from funciones import *

MAX_INTENTOS = 3

def autenticar():
    intentos = 0

    while intentos < MAX_INTENTOS:
        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()

        usuario = input(f"{VERDE}👤 Ingrese su usuario:{BLANCO} \n").lower().strip()
        Limpiar_pantalla()
        cargar()
        Limpiar_pantalla()

        if usuario not in CUENTAS:
            intentos += 1

            print(f"{ROJO}❌ Usuario incorrecto{AMARILLO}\n")
            print(f"Intentos restantes: {MAX_INTENTOS - intentos}{VERDE}\n")
            input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")

            Limpiar_pantalla()
            cargar()
            Limpiar_pantalla()
            
        
            if intentos == MAX_INTENTOS:

                print(f"{ROJO}🔒 Cajero bloqueado temporalmente por demasiados intentos.{AMARILLO}")
                input(f"Presione Enter para continuar...{VERDE}")
                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
                return 
            
            continue
        
        while intentos < MAX_INTENTOS:


            pin = input(f"{VERDE}🔒 Ingrese su PIN de 4 números:{BLANCO} \n").strip()
            Limpiar_pantalla()
            cargar()
            Limpiar_pantalla()

            if not pin.isdigit():
                intentos += 1

                print(f"{ROJO}⚠ Error: El PIN solo puede contener numeros.{AMARILLO}")
                print(f"Intentos restantes: {MAX_INTENTOS - intentos}")
                input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")

                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
                if intentos == MAX_INTENTOS:
                    print(f"{ROJO}🔒 Cuenta bloqueada temporalmente por demasiados intentos de PIN.{AMARILLO}")
                    input(f"Presione Enter para continuar...{VERDE}")
                    return None
                continue

            if len(pin) != 4:
                intentos += 1

                print(f"{ROJO}⚠ Error: El PIN debe tener exactamente 4 digitos.{AMARILLO}")
                print(f"Intentos restantes: {MAX_INTENTOS - intentos}{VERDE}")
                input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")

                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
                if intentos == MAX_INTENTOS:
                    print(f"{ROJO}🔒 Cuenta bloqueada temporalmente por demasiados intentos de PIN.{AMARILLO}")
                    input(f"Presione Enter para continuar...{VERDE}")
                    return None
                continue

            if CUENTAS[usuario]["clave"] == pin:
                print("✅ Autenticación exitosa\n")
                input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
                return usuario

            else:
                print("❌ PIN incorrecto")
                intentos += 1
                print(f"Intentos restantes: {MAX_INTENTOS - intentos}")

                if intentos == MAX_INTENTOS:
                    print(f"{ROJO}🔒 Cuenta bloqueada temporalmente por demasiados intentos de PIN.{AMARILLO}")
                    input(f"{AMARILLO}Presione Enter para continuar...{VERDE}")
                    return None
                input(f"{AMARILLO}Presione Enter para Salir...{VERDE}")
                Limpiar_pantalla()
                cargar()
                Limpiar_pantalla()
