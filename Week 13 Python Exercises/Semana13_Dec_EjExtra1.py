def repeat_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper

@repeat_twice
def print_name(Name, last_name):
    print(f"Hola {Name} {last_name}")

print_name("Steven", "Quiros")