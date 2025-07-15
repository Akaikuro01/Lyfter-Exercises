import random

secret_number = random.randint(1, 10)
number = 0
correct = False

number = int(input("Digite un numero"))
while(correct == False):
    if (number == secret_number):
        correct = True
    else:
        number = int(input("Digite un numero"))

print("Acertado!!")

