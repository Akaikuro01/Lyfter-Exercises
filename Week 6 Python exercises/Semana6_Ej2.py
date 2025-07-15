global_var = 11

def this_function():
    variable_func = 0
    global global_var
    global_var = 8
    return

this_function()
print(global_var)

