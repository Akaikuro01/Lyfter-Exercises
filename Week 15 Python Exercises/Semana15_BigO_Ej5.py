def print_all_pairs(my_dict):
    for key1 in my_dict:
        for key2 in my_dict:
            print(f"{key1}-{key2}")

my_dict = {
    "A": 1,
    "B": 2,
    "C": 3
}

print_all_pairs(my_dict)

# El algoritmo imprime todas las parejas posibles de keys en el diccionario.
# Esto significa que a más keys tenga el diccionario, el número de iteraciones crece de forma cuadrática O(n^2).
# ¿Cuánto tiempo con un millón de keys? Para 1,000,000 de keys, serían 1,000,000^2 = 1,000,000,000,000 iteraciones.
# El tiempo exacto dependerá del rendimiento del equipo, pero sería muy alto y poco práctico de ejecutar.