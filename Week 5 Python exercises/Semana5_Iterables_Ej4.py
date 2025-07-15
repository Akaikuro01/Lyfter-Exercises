my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_list)

for index, element in enumerate(my_list):
    if (my_list[index] % 2 > 0):
        my_list.pop(index)

print(my_list)