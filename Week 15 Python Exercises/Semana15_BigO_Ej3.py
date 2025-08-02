# manual_add: O(n) -> Un bucle recorre todos los números hasta n (lento para valores grandes)
def manual_add(number):
    result = 0 # O(1)
    for i in range(1, number + 1): # O(n)
        result += i # O(1)
    return result # O(1)

# add_formula: O(1) -> Usa una fórmula directa sin bucles (rápido incluso para valores muy grandes)
def add_formula(number):
    return number * (number + 1) // 2 # O(1)

# Para n = 1,000,000,000 se elige add_formula porque evita mil millones de iteraciones