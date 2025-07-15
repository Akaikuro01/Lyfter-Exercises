seconds = 0
remaining = 0

seconds = int(input("Digite una cantidad en segundos: "))

if (seconds < 600):
    remaining = 600 - seconds
    print(f"Segundos faltantes para llegar a 10 minutos: {remaining}")
elif (seconds == 600):
    print("Igual.")
else:
    print("Mayor.")
