user_list = []
counter = 1
highest_number = 0

while(counter <= 10):
    user_list.append(int(input("Digite un numero: ")))
    counter = counter + 1

for index, element in enumerate(user_list):
        if(user_list[index] > highest_number):
            highest_number = user_list[index]

print(f"{user_list}. El mas alto fue {highest_number}")