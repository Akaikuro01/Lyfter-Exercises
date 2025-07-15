num1 = 0
num2 = 0
num3 = 0
accumulated = 0

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))
num3 = int(input("Digite un numero: "))

if (num1 == 30 or num2 == 30 or num2 == 30):
    print("Correcto!!")
else:
    accumulated = num1 + num2 + num3
    if (accumulated == 30):
        print("Correcto!!")
    else:
        print("Incorrecto :(")