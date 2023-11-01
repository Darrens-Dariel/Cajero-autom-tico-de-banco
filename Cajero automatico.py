Saldo = 1000

while True:
    print("BIENVENIDO AL CAJERO AUTOMÁTICO")
    print(" (1). Ingresar dinero")
    print(" (2). Retirar dinero")
    print(" (3). Ver saldo")
    print(" (4). Salir")
    
    seleccionar = int(input("Elija una opción: "))

    if seleccionar == 1:
        ingreso = float(input("Ingrese Dinero: "))
        if ingreso > 0:
            Saldo += ingreso
            print(f"Su saldo ingresado es de: {ingreso}. Su nuevo saldo es de: {Saldo}")
        else:
            print("Error: Ingrese un número mayor a 0.")

    elif seleccionar == 2:
        retirar = float(input("Dinero a Retirar: "))
        if retirar > 0:
            if retirar <= Saldo:
                Saldo -= retirar
                print(f"Usted retiro: {retirar} su nuevo saldo es de: {Saldo}")
            else:
                print ("Saldo Insuficiente para retirar")
        else:
            print("Ingrese un numero mayor a 0 para rerirar")
            
    elif seleccionar == 3:
        print(f"Su saldo actual es de: {Saldo}")

    elif seleccionar == 4:
        print("Saliendo del cajero automático. ¡Hasta luego!")
        break  

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

print("Programa finalizado.")


   

    

