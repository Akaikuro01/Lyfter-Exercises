user_logged_in = False

def requires_login(func):
    def wrapper(*args, **kwargs):
        global user_logged_in
        try:
            if(user_logged_in == False):
                raise Exception("Usuario no autenticado")
            else:
                func(*args, **kwargs)
        except Exception as ex:
            print(ex)
    return wrapper

@requires_login
def view_profile():
    print("Mostrando perfil del usuario")

view_profile()