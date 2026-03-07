# Simulador de cajero automático

## Descripción del proyecto 
Este proyecto consiste en la elaboración de un cajero automático haciendo uso de herramientas como Python, Git y GitHub.

El simulador permite a los usuarios realizar funciones como:
 1. Consultar saldo 
 2. retirar/depositar saldo  
 3. salir del programa. 
 
 Esto, teniendo en cuenta la aplicación de las reglas de negociación y las validaciones específicas en lo que respecta a la entrada de números.

## Objetivo

Poner en práctica habilidades como:

1. Trabajo colaborativo: Ya que, se hizo uso de GitHub y Trello.

2. Validación de datos.

3. Validación de reglas de negociación.

## Funcionalidades

El proyecto "Simulador de cajero automático" cumple con las siguientes funciones:

1. Muestra un mensaje de bienvenida.
2. Solicita autenticación al usuario.
3. Valida intentos.
4. Le indica al usuario cuántas operaciones quiere realizar.
5. Muestra el menú por cada operación que el usuario realice
6. Ejecuta la acción que se le indique.
7. Valida las reglas de negociación.
8. Finaliza cuando el usuario le indique o cuando termine de ejecutar una operación.
9. Muestra un mensaje final de agradecimiento.

## Reglas de negocio

1. El sistema inicia con un saldo fijo de $1000
2. El usuario se autentica con un pin 
3. El usuario tiene un límite de intentos
4. El sistema realiza bien sus funciones
5. No permite montos negativos
6. No permite retiros mayores al saldo disponible
7. Cuando finaliza muestra un mesaje de despedida
8. El sistema se ejecuta desde un archivo llamado main.py