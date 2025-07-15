list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}

print(employee)

for index, key in enumerate(list_of_keys):
    employee.pop(key)

print(employee)