def count_lower_upper_case_in_String(the_word):
    upper_count = 0
    lower_count = 0
    for char in the_word:
        if (char.isupper()):
            upper_count += 1
        elif(char.islower()):
            lower_count += 1

    print(f"I found {upper_count} upper case letters and {lower_count} lower case letters.")


count_lower_upper_case_in_String("I want to become the PIRATE KING!!")