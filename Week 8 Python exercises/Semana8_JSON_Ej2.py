import json

def read_json_into_dict(path):
    try:
        pokemon_dict = []
        with open(path) as file:
            pokemon_dict = json.load(file)
        print(type(pokemon_dict))
        return pokemon_dict
    except Exception as ex:
        print(ex)



def ask_new_pokemon():
    try:
        name = input("Digite el nombre del Pokemon a ingresar: ")
        type_str = input("Digite el tipo del Pokemon que desea ingresar (Separar por un espacio si es mas de uno. Eg: Rock Fire): ")   
        type_list = []
        base = {}
        hp = int(input("Digite la cantidad de HP del nuevo Pokemon: "))
        attack = int(input("Digite la cantidad de ataque del nuevo Pokemon: "))
        defense = int(input("Digite la cantidad de defensa del nuevo Pokemon: "))
        sp_attack = int(input("Digite la cantidad de Sp. attack del nuevo Pokemon: "))
        sp_defense = int(input("Digite la cantidad de Sp. Defense del nuevo Pokemon: "))
        speed = int(input("Digite la cantidad de velocidad del nuevo Pokemon: "))

        type_to_add = ""
        length_type = len(type_str)
        for index, char in enumerate(type_str):
            if char != ' ':
                type_to_add += char
                if (index == length_type - 1):
                    type_list.append(type_to_add)
                    type_to_add = "" 
            elif (char == ' '):
                type_list.append(type_to_add)
                type_to_add = ""   


        name_dict = {"english": name}
        base = {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "Sp. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }

        new_pokemon = {
            "name": name_dict,
            "type": type_list,
            "base": base
        }

        return new_pokemon
    except Exception as ex:
        print(ex)

def insert_new_pokemon_to_json(path, final_pokemon_list):
    try:
        with open(path, 'w', encoding="utf-8") as file:
            json.dump(final_pokemon_list, file, indent=2)
    except Exception as ex:
        print(ex)
        


def add_pokemons_to_json(path):
    try:
        pokemon_dict = []
        pokemon_dict = read_json_into_dict(path)
        new_pokemon = ask_new_pokemon()

        pokemon_dict.append(new_pokemon)
        insert_new_pokemon_to_json(path, pokemon_dict)
    except Exception as ex:
        print(ex)


add_pokemons_to_json("D:\Documents\Lyfter\Week 8 Python exercises\Pokemons.json")