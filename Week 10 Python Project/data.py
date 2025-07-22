import actions
import csv

def export_data_student_CSV(path, list_students, headers):
	try:
		with open(path, 'w', encoding='utf-8', newline='') as file:
			writer = csv.DictWriter(file, headers)
			writer.writeheader()
			writer.writerows(list_students)
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
				student_list.append(row)
		
		return student_list
	except Exception as ex:
		print(ex)

