from usuarios import CUENTAS

MAX_INTENTOS = 3

def autenticar():
    intentos = 0

    while intentos < MAX_INTENTOS:

        usuario = input("Ingrese su usuario: \n").strip()

        if usuario not in CUENTAS:
            intentos += 1
            print("❌ Usuario incorrecto")
            print(f"Intentos restantes: {MAX_INTENTOS - intentos}")
            
        
            if intentos == MAX_INTENTOS:
                print("🔒 Cajero bloqueado temporalmente por demasiados intentos.")
                return None
            
            continue
        
        while intentos < MAX_INTENTOS:

            pin = input("Ingrese su PIN de 4 números: \n").strip()

            if not pin.isdigit():
                intentos += 1
                print("⚠ Error: El PIN solo puede contener numeros.")
                print(f"Intentos restantes: {MAX_INTENTOS - intentos}")
                continue

            if len(pin) != 4:
                intentos += 1
                print("⚠ Error: El PIN debe tener exactamente 4 digitos.")
                print(f"Intentos restantes: {MAX_INTENTOS - intentos}")
                continue

            if CUENTAS[usuario]["clave"] == pin:
                print("✅ Autenticación exitosa")
                return usuario

            else:
                print("❌ PIN incorrecto")
                intentos += 1
                print(f"Intentos restantes: {MAX_INTENTOS - intentos}")

                if intentos == MAX_INTENTOS:
                    print("🔒 Cuenta bloqueada temporalmente por demasiados intentos de PIN.")
                    return None
                
if __name__ == "__main__":    
    autenticar()