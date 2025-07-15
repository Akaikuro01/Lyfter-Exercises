import math

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

print(choose_prime_numbers([1, 4, 6, 7, 13, 9, 67]))

