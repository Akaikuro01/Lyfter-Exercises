age = 0
name = "" 
last_name = ""

name = input("Digite su nombre")
last_name = input("Digite su apellido")
age = int(input ("Digite su edad"))

if (age <= 2):
    print(f"{name} usted es un bebé")
elif (age >= 3 and age <= 6):
    print(f"{name} usted es un niño")
elif (age >= 7 and age <= 12):
    print(f"{name} usted es un preadolescente")
elif (age >= 13 and age <= 17):
    print(f"{name} usted es un Adolescente")
elif (age >= 18 and age <= 29):
    print(f"{name} usted es un adulto joven")
elif (age >= 30 and age <= 59):
    print(f"{name} usted es un adulto")
elif (age >= 60):
    print(f"{name} usted es un niño")
