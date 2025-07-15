def print_backwards(my_string):
    for index in range(len(my_string) - 1, -1, -1):
        print(my_string[index])
    return my_string

print_backwards("I love turtles")