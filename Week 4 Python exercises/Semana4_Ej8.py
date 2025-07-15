number = 0
counter = 1
accumulated = 0

number = int(input("Digite un numero: "))
while (counter <= number):
    accumulated = counter + accumulated
    counter = counter + 1

print(accumulated)