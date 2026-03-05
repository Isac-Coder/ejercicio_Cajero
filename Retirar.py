#Consultar saldo

from Validaciones import pedir_numero
    
def retirar_dinero(usuario, CUENTAS):
    retirar = pedir_numero("Ingrese el valor que desea retirar: ")

    if retirar <= 0:
        print("No se permiten montos negativos o cero.")

    elif retirar > CUENTAS[usuario]["saldo"]:
        print("No se puede retirar más del saldo disponible.")

    elif retirar != int:
        print("Porfavor ingrese un monto valido.")
    else:
        CUENTAS[usuario]["saldo"] -= retirar
        print("Retiro exitoso.")
        print("Su nuevo saldo es:", CUENTAS[usuario]["saldo"]) 
        







   
    
    
        
        
        
    



