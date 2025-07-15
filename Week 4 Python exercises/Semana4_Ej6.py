product_price = 0
discount = 0
final_price = 0

product_price = int(input("Digite el precio del producto: "))

if(product_price >= 100):
    discount = 0.10
else:
    discount = 0.02

final_price = product_price - (product_price * discount)
print(f"El precio final del producto es de: {final_price}")