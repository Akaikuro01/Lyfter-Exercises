def calculator():
    current_number = 0
    while (True):
        try:
            print("""===========================
Calculadora de Consola
===========================
        """)
            
            
            print(f"Numero actual: {current_number}")
            print(""" Seleccione una operacion: 
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Borrar resultado
        6. Salir
    """)

            option = int(input("Opcion: "))
            if (option < 1 or option > 6):
                raise ValueError("Digite una opcion valida del menu")
            match option:
                case 1: 
                    current_number = current_number + int(input("Ingrese numero a sumar: "))
                    print(f"Resultado: {current_number}")
                    print("")
                case 2: 
                    current_number = current_number - int(input("Ingrese numero a restar: "))
                    print(f"Resultado: {current_number}")
                    print("")
                case 3: 
                    current_number = current_number * int(input("Ingrese numero a multiplicar: "))
                    print(f"Resultado: {current_number}")
                    print("")
                case 4: 
                    current_number = current_number / int(input("Ingrese numero a dividir: "))
                    print(f"Resultado: {current_number}")
                    print("")
                case 5: 
                    current_number = 0     
                    print("Resultado reiniciado a 0")
                    print("")
                case 6:
                    break
        except ValueError as ex:
            print(f"La opcion digitada no es valida: {ex}")
        except ZeroDivisionError as ex:
            print("No puedo dividir entre 0")


calculator()