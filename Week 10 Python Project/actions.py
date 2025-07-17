def add_students_to_list(list_students):
    try:
        students_dict = {}
        name = input("Digite el nombre del estudiante a ingresar: ")
        homeroom = input("Digite la seccion del estudiante a ingresar: ")
        spanish_grade = float(input("Digite la nota de Español del estudiante a ingresar: "))
        if (spanish_grade < 0 or spanish_grade > 100):
            raise ValueError ("Digite una nota del 0 al 100.")
        english_grade = float(input("Digite la nota de Ingles del estudiante a ingresar: "))
        if (english_grade < 0 or english_grade > 100):
            raise ValueError ("Digite una nota del 0 al 100.")
        social_studies_grade = float(input("Digite la nota de Estudios Sociales del estudiante a ingresar: "))
        if (social_studies_grade < 0 or social_studies_grade > 100):
            raise ValueError ("Digite una nota del 0 al 100.")
        science_grade = float(input("Digite la nota de Ciencias del estudiante a ingresar: "))
        if (science_grade < 0 or science_grade > 100):
            raise ValueError ("Digite una nota del 0 al 100.")

        students_dict = {
            "Nombre": name,
            "Seccion": homeroom,
            "Nota espanol": spanish_grade,
            "Nota ingles": english_grade,
            "Nota estudios sociales": social_studies_grade,
            "Nota ciencias": science_grade 
        }

        list_students.append(students_dict)
        return list_students
    except ValueError as ex:
        print(ex)




def see_students_list(list_students):
    try:
        if (list_students == [] or list_students is None):
            raise Exception ("Actualmente no hay estudiantes en el sistema.")
        student = {}
        for index, student in enumerate(list_students):
            student = list_students[index]
            for key, values in student.items():
                print(f"{key}: {values}")
    except Exception as ex:
        print(ex)



def calculate_avg_grade_students(list_students):
    try:
        if (list_students == [] or list_students is None):
            raise Exception ("Actualmente no hay estudiantes en el sistema.")
        avg_grade_students_list = []
        avg_student_dict = {}
        accumulated_grade = 0
        avg_grade = 0
        for index, student in enumerate(list_students):
            for value in student.values():
                if (check_value_type(value)):
                    accumulated_grade += float(value)
            avg_grade = accumulated_grade / 4
            avg_student_dict = {
                "Nombre": student["Nombre"],
                "Promedio": avg_grade
            }
            avg_grade_students_list.append(avg_student_dict)
            accumulated_grade = 0
        return avg_grade_students_list
    except KeyError as ex:
        print(ex)
    except ZeroDivisionError as ex:
        print(ex)
    except ValueError as ex:
        print(ex)
    except TypeError as ex:
        print(ex)
    except Exception as ex:
        print(ex)



def see_avg_grade_students_list(avg_grade_students_list):
    try:
        student = {}
        for index, student in enumerate(avg_grade_students_list):
            student = avg_grade_students_list[index]
            for key, values in student.items():
                print(f"{key}: {values}")
    except Exception as ex:
        print(ex)



def calculate_avg_top_3_students(avg_grade_students_list): 
    try:
        top_3_student_avg = []
        highest_avg = 0
        while(True):        
            if (len(avg_grade_students_list) == 0):
                break
            for index, student in enumerate(avg_grade_students_list):
                avg_student_grade = student["Promedio"]
                if(avg_student_grade >= highest_avg or highest_avg == 0):
                    highest_avg = avg_student_grade
                    index_highest_avg = index
            
            top_3_student_avg.append(avg_grade_students_list.pop(index_highest_avg))
            highest_avg = 0
            if(len(top_3_student_avg) == 3):
                break
        


        return top_3_student_avg
    except Exception as ex:
        print(ex)



def convert_values_dict_to_floats(students_list):
    try:
        fixed_students_dict = {}
        fixed_students_list = []
        for student in students_list:
            for key, value in students_list.items():
                if(check_value_type(value)):
                    fixed_students_list[key] = float(value)
                else:
                    fixed_students_list[key] = value
            fixed_students_list.append(fixed_students_dict)
            fixed_students_dict = {}

        return fixed_students_list
    except Exception as ex:
        print(ex)



def check_value_type(value):
	try:
		float(value)
		return True
	except ValueError as ex:
		return False

