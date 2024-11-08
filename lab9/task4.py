menu = [
    ["Пицца Маргарита", ["мука", "томаты", "сыр", "базилик"], 10],
    ["Салат Цезарь", ["салат", "курица", "сыр", "сухарики"], 8],
    ["Суп Томатный", ["томаты", "лук", "морковь", "картофель"], 6]
]

def print_menu_item(item):
    print(item[0])
    print("Состав: ", ", ".join(item[1]))
    print(f"Цена: {item[2]}")

def print_menu(menu):
    for i in range(len(menu)):
        print_menu_item(menu[i])
        if i != len(menu) - 1:
            print("\n\n***\n")

def find_menu_item_by_name(menu, name):
    filtered = list(filter(
        lambda x: x[0].lower().find(name.lower()) != -1, 
        menu
    ))

    if len(filtered > 0):
        return filtered[0]
    else:
        return -1

def add_menu_item(name, ingredients, price):
    menu.append([
        name,
        ingredients,
        price
    ])

def input_menu_item():
    name = input("Какое блюдо вы хотите добавить?\n> ")
    price = int(input("Сколько будет стоить блюдо?\n> "))
    ingredients_count = max(int(input("Сколько в блюде ингредиентов?\n> ")), 1)
    ingredients = []
    print("Введите ингредиенты:")
    for _ in range(ingredients_count):
        ingredients.append(input("> "))

    add_menu_item(name, ingredients, price)

def change_menu_item_price(name, new_price):
    item = find_menu_item_by_name(menu, name)
    item

get_menu_item(menu, "Пицца")