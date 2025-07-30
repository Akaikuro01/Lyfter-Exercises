from datetime import date

class User:
    date_of_birth: date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )


def my_decorator(func):
        def wrapper(user):
            try:
                if(user.age < 18):
                    raise ValueError (f"Usted no es mayor de edad: {user.age}")
                return func(user)
            except ValueError as ex:
                print(ex)
        return wrapper


@my_decorator
def check_age(user):
    print(f"Usted es mayor edad: {user.age}")


my_user = User(date(2020, 1, 1))
check_age(my_user)