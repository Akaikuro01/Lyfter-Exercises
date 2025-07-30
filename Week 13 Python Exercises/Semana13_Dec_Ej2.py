def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                for arg in args:
                    if not isinstance(arg, (int, float)):
                        raise ValueError("The parameter provided is not a number") 
                
                for value in kwargs.values():
                    if not isinstance(value, (int, float)):
                        raise ValueError("The parameter provided is not a number") 
                return func(*args, **kwargs)         
            except ValueError as ex:
                print(ex)
        return wrapper


@my_decorator
def numbers_function(number1, number2, number3):
    print(f"Numbers received: {number1}, {number2}, {number3}")



numbers_function("4", 4, 4)
numbers_function(number1="4", number2=4, number3=4)
numbers_function(4, number2=4, number3=4)  