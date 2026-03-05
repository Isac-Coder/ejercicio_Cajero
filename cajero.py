def retirar_dinero(saldo):
    retirar = int(input("Ingrese el valor que desea retirar \n")) 

    if retirar < 0:
     print("Monto no válido")
    
    elif retirar > saldo: 
        print("No se puede retirar el monto ingresado")    
    
    else:
        print("Su retiro ha sido de:", retirar)     
        







   
    
    
        
        
        
    



