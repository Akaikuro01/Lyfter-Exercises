from datetime import datetime
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        date = datetime.now()
        func_name = func.__name__
        result = func(*args, **kwargs) 
        print(f"{date}, {func_name}, arguments: {args} {kwargs}, Resultado: {result}")       
        print(f"Resultado: {result}")
        return result
    return wrapper

def validate_numbers(func):
    @wraps(func)
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


@validate_numbers
@log_call
def multiply(number1, number2):
    result = number1 * number2
    return result


multiply(5, 7)