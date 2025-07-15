my_list = [4, 3, 6, 1, 7]

print(my_list)

first_element = my_list.pop(0)
last_element = my_list.pop(len(my_list) - 1)

my_list.insert(0, last_element)
my_list.append(first_element)

print(my_list)