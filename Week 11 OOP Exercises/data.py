import actions
import csv

def export_data_student_CSV(path, list_students):
	try:
		list_students_dict = []
		student_dict = {}
		for student in list_students:
			student_dict = {
            "Nombre": student.name,
            "Seccion": student.homeroom,
            "Nota espanol": student.spanish_grade,
            "Nota ingles": student.english_grade,
            "Nota estudios sociales": student.social_studies_grade,
            "Nota ciencias": student.science_grade 
        	}
			list_students_dict.append(student_dict)
		with open(path, 'w', encoding='utf-8', newline='') as file:
			writer = csv.DictWriter(file, list_students_dict[0].keys())
			writer.writeheader()
			writer.writerows(list_students_dict)
	except FileNotFoundError as ex:
		print(ex)
	except PermissionError as ex:
		print(ex)


def import_CSV_into_list(path):
	try:
		student_list = []
		student_dict = {}
		with open(path) as file:
			reader = csv.DictReader(file)
			for row in reader:		
				new_student = actions.Student(row["Nombre"], row["Seccion"], row["Nota espanol"], row["Nota ingles"], row["Nota estudios sociales"], row["Nota ciencias"])		
				student_list.append(new_student)
		
		return student_list
	except Exception as ex:
		print(ex)

