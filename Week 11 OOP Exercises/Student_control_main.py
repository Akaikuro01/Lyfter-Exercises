import menu

def main():
    try:
        print("""======================================
Bienvenido al sistema de control de estudiantes.
======================================
                """)
        
        menu.execute_option_from_menu()
    except Exception as ex:
        print(ex)



main()
