def my_decorator(func):
    def wrapper(*args):
        print(f"Called with args: {args}")
        result = func(*args)
        print(f"Returned: {result}")
        return result
    return wrapper


@my_decorator
def my_function(kono, giorno, giovana, niwa, yume, ga, aru):
    return f"{kono} {giorno} {giovana} {niwa} {yume} {ga} {aru}"

my_function("kono", "Giorno", "Giovanna", "ni wa,", "yume", "ga", "aru")