import actions
import data

def select_option_menu():
    try:
        option = int(input("""Seleccione una opcion del menu: 
            1. Ingresar un nuevo estudiante.
            2. Ver informacion de estudiantes.
            3. Ver el top 3 de estudiantes con mejores promedios.
            4. Ver promedios de todos los estudiantes.
            5. Exportar datos actuales a un archive CSV.
            6. Importar datos desde un archivo CSV.
            7. Salir

            """))
        if(option < 0 or option > 7):
            raise ValueError ("Digite una opcion valida.")
        return option
    except ValueError as ex:
        print(ex)


def execute_option_from_menu():
    try:
        student_list = []
        while(True):
            option = select_option_menu()
            match option:
                case 1:
                    while(True):
                        actions.add_students_to_list(student_list)                        
                        while(True):
                            add_anoter_student = input("Desea ingresar un nuevo estudiante? Y = Si, N = No: ")
                            if (add_anoter_student != "Y" and add_anoter_student != "N"):
                                print("Digite una opcion valida (Y/N)")
                            elif (add_anoter_student == "Y" or add_anoter_student == "N"):
                                break
                        if add_anoter_student == "N":
                            break
                        
                case 2:
                    actions.see_students_object(student_list)
                case 3:
                    avg_grade_students_list = actions.calculate_avg_grade_students(student_list)
                    top_3_students_list = actions.calculate_avg_top_3_students(avg_grade_students_list)
                    actions.see_students_list(top_3_students_list)
                case 4:
                    avg_grade_students_list = actions.calculate_avg_grade_students(student_list)
                    print(f"El promedio del total de todos los promedios de los alumnos es de: {actions.calculate_avg_all_students(avg_grade_students_list)}")
                case 5:                    
                    data.export_data_student_CSV("Estudiantes.csv", student_list)
                    print("Datos fueron exportados.")
                case 6:
                    student_list = data.import_CSV_into_list("Estudiantes.csv")
                    print("Datos fueron importados.")
                case 7:
                    print("Muchas gracias por usar nuestro sistema!")
                    break
    except Exception as ex:
        print(ex)
