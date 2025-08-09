import math

def sum_numbers(number_list):
    accumulated_value = 0
    for index, number in enumerate(number_list):
        accumulated_value += number
    return accumulated_value


def print_backwards(my_string):
    for index in range(len(my_string) - 1, -1, -1):
        print(my_string[index])
    return my_string


def count_lower_upper_case_in_String(the_word):
    upper_count = 0
    lower_count = 0
    for char in the_word:
        if (char.isupper()):
            upper_count += 1
        elif(char.islower()):
            lower_count += 1


def order_string_alphabetically(the_String):
    list_of_words = []
    words_to_add = ""
    final_string = ""
    string_to_add = ""

    for char in the_String:
        if (char != '-'):
            words_to_add += char
        else:
            list_of_words.append(words_to_add)
            words_to_add = ""
    list_of_words.append(words_to_add )


    lowest_number = 0
    lowest_word_index = 0
    counter = 1

    while (True):
        if(len(list_of_words) == 0):
            break
        else:
            for index, word in enumerate(list_of_words):
                number = ord(word[0])
                if (number < lowest_number or lowest_number == 0):
                    lowest_number = number
                    lowest_word_index = index

        string_to_add = list_of_words.pop(lowest_word_index)
        
        final_string += string_to_add
        if (len(list_of_words) > 0):
            final_string += "-"
            lowest_number = 0
        
    print(final_string)


def choose_prime_numbers(number_list):
    list_of_primes = []
    for number in number_list:
        if(check_prime_numbers(number) == True):
            list_of_primes.append(number)
    
    return list_of_primes


def check_prime_numbers(number):
    if (number <= 0):
        return False
    
    if(number == 1):
        return False

    if (number == 2):
        return True
    
    if (number > 2 and number % 2 == 0):
        return False
    
    divisibility = int(math.sqrt(number))
    divider = 3
    while (divider <= divisibility):
        if(number % divider == 0):
            return False
            break
        
        divider += 1
            
    return True


print_backwards("A ")

