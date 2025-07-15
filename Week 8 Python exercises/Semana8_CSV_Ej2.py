import csv


def request_amount_games_menu():
    try:
        amount_games = int(input("Digite la cantidad de juegos que desea ingresar: " ))
        return amount_games
    except Exception as ex:
        print(ex)



def add_games_to_dict(amount_games):
    try:
        counter = 0
        name = ""
        genre = ""
        developer = ""
        rating = ""
        games_dict = {}
        games_list = []
        while(counter < amount_games):
            name = input("Digite el nombre del juego: ")
            genre = input("Digite el genero del juego: ")
            developer = input("Digite el nombre del desarrollador del juego: ")
            rating = input("Digite la clasificacion del juego: ")

            games_dict = {
                "name": name,
                "genre": genre,
                "developer": developer,
                "rating ESRB": rating
            }
            games_list.append(games_dict)
            counter += 1

        
        return games_list
    except Exception as ex:
        print(ex)



def write_csv_file (path, data, headers):
    with open(path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, headers, delimiter='\t')
        writer.writeheader()
        writer.writerows(data)



def add_games_to_csv(path):
    try:
        amount_games = request_amount_games_menu()
        games_list = add_games_to_dict(amount_games)
        write_csv_file(path, games_list, games_list[0].keys())
    except Exception as ex:
        print(ex)



add_games_to_csv("D:\Documents\Lyfter\Week 8 Python exercises\games_tab.csv")
