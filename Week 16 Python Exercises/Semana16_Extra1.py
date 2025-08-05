def add_numbers(a, b):
    return a + b

def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
