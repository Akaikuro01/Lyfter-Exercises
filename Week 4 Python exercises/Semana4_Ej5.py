total_grades = 0
grades = []
passed = []
failed = []
total_passed = 0
added_total = 0
added_passed = 0
total_failed = 0
added_failed = 0
average_total = 0
average_passed = 0
average_failed = 0
counter = 1

total_grades = int(input("Digite cuantas notas quiere revisar: "))

while(counter <= total_grades):
    grades.append(int(input("Digite nota: ")))
    counter = counter + 1

for index, grade in enumerate(grades):
    added_total = added_total + grades[index]
    if (grades[index] >= 70):
        total_passed = total_passed + 1
        passed.append(grades[index])
    else:
        total_failed = total_failed + 1
        failed.append(grades[index])

for index, grade in enumerate(passed):    
    added_passed = added_passed + passed[index]

for index, grade in enumerate(failed):    
    added_failed = added_failed + failed[index]

if (total_failed > 0 and total_passed > 0):
    average_passed = added_passed / total_passed
    average_failed = added_failed / total_failed
    average_total = added_total / total_grades
    print (f"""Usted tiene {total_passed} notas aprobadas.
Usted tiene {total_failed} notas reprobadas.
El promedio de todas sus notas es de: {average_total}.
El promedio de sus notas aprobadas es de: {average_passed}
El promedio de sus notas reprobadas es de: {average_failed} """)
elif (total_failed == 0):
    average_passed = added_passed / total_passed
    average_total = added_total / total_grades
    print (f"""Usted tiene {total_passed} notas aprobadas.
Usted tiene {total_failed} notas reprobadas.
El promedio de todas sus notas es de: {average_total}.
El promedio de sus notas aprobadas es de: {average_passed} """)
elif (total_passed == 0):
    average_failed = added_failed / total_failed
    average_total = added_total / total_grades
    print (f"""Usted tiene {total_passed} notas aprobadas.
Usted tiene {total_failed} notas reprobadas.
El promedio de todas sus notas es de: {average_total}.
El promedio de sus notas reprobadas es de: {average_failed} """)



