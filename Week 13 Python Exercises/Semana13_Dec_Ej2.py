def my_decorator(func):
        def wrapper(*args):
            try:
                for arg in args:
                    if not isinstance(arg, (int, float)):
                        raise ValueError("The parameter provided is not a number") 
                return func(*args)
            except ValueError as ex:
                print(ex)
        return wrapper


@my_decorator
def numbers_function(number1, number2, number3):
    print(f"Numbers received: {number1}, {number2}, {number3}")



numbers_function("4", 4, 4)