# Esta funcion se encarga de recorrer la lista hasta encontrar el "target", es bastante simple en terminos de complejidad ya que solo recorre la list uno a uno, sin embargo en listas muy grandes, podria tardar mas. El beneficio de esta 
# es que no necesita tener una lista ya ordenada para poder encontrar el target.
def linear_search(my_list, target):
    for item in my_list:
        if item == target:
            return True
    return False

# Esta funcion funciona solo para listas ya ordenadas y divide la cantidad de iteraciones cada vez, por lo que es O(log n), 
# mientras que en si es mas compleja, para listas ya ordenadas, es ams eficiente ya que no tiene que hacer tantas iteraciones como ir elemento por elemento hasta encontrar el target.
def binary_search(my_list, target):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if my_list[mid] == target:
            return True
        elif my_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


binary_search([54,6,78,34,3,22,5], 5)

# En conclusion, es mejor usar el binary search para listas ordenadas, o si son muy grandes, usar el metodo de sort de python y luego correr esta. Para listas que son mas pequeñas y no estan ordenadas, seria mejor usar linear search.