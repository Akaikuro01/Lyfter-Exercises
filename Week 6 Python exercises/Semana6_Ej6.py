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
        

order_string_alphabetically("python-variable-funcion-computadora-monitor")

