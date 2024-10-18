product = input("Товар: ")
price = float(input("Цена: "))
discount = 0

if product == "сланцы" or product == "шорты" or product == "кепка":
    if price > 1000:
        discount = 10
    elif price > 2000:
        discount = 15

if discount > 0:
    print(f"Цена: {price}\nСкидка: {discount}%\nЦена со скидкой: {price * discount / 100.0}")
else:
    print(f"Цена: {price}")

