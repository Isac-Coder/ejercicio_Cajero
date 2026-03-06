def pedir_numero(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")

def pedir_texto(mensaje):
    while True:
        try:
            valor = str(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Debe ingresar un teto.")