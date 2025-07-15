list_a = ["first_name", "last_name", "role"]
list_b = ["Steven", "Quiros", "SQL Support engineer"]
person = {}

for index, value in enumerate(range(0, len(list_a))):
    person[list_a[index]] = list_b[index]

print(person)