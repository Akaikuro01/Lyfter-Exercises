current_number = 0
previous_number = 0
counter = 1
highest_number = 0

while(counter <= 3):
    current_number = int(input("Digite un numero"))
    if(current_number > highest_number):
        highest_number = current_number
        previous_number = current_number
        counter = counter + 1
    else:
        previous_number = current_number
        counter = counter + 1

print(highest_number)
