def select_option_from_menu():
    try:         
        print("""Seleccione una operacion: 
        1. Suma
        2. Resta
        3. Multiplicación
        4. División
        5. Borrar resultado
        6. Salir
        """)
        
        option = float(input("Opcion: "))
        if (option < 1 or option > 6):
                raise ValueError("Digite una opcion valida del menu") 
        return option
    except ValueError as ex:
        print(f"Digite una opcion valida del menu")



def request_number():
    try:
        return float(input("Digite numero a operar: "))
    except ValueError as ex:
        print(f"La opcion digitada no es valida: {ex}")


def calculate_operation(option, current_number, requested_number):
    try:
        result = 0
        match option:
            case 1:
                result = current_number + requested_number
                return result
            case 2:
                result = current_number - requested_number
                return result
            case 3:
                result = current_number * requested_number
                return result
            case 4:
                result = current_number / requested_number
                return result
            
    except ValueError as ex:
        print(f"Hubo un error: {ex}")
    except ZeroDivisionError as ex:
        print("No puedo dividir entre 0")

def show_current_number(current_number):
    try:
        print(f"Numero actual: {float(current_number)}")
    except Exception as ex:
        print(f"Hubo un error: {ex}")


def calculator():
    try:
        print("""===========================
Calculadora de Consola
===========================
            """)
        current_number = 0
        while (True):
            show_current_number(current_number)        
            option = select_option_from_menu()
            if option is None:
                continue
            elif option == 5:
                current_number = 0
                print("resultado reiniciado a 0.0")
                print("")
                continue

            if(option == 6):
                break
            
            number = request_number()
            current_number = calculate_operation(option, current_number, number)
            if (current_number is None):
                current_number = 0
    except Exception as ex:
        print(f"Hubo un error: {ex}")


calculator()
