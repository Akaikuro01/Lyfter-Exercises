def sum_numbers(number_list):
    accumulated_value = 0
    for index, number in enumerate(number_list):
        accumulated_value += number
    return accumulated_value


print(sum_numbers([100, 100, 100, 100]))
