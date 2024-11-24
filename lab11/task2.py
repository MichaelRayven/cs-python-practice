points = {
    "A": 1,
    "E": 1,
    "I": 1,
    "L": 1,
    "N": 1,
    "O": 1,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "D": 2,
    "G": 2,
    "B": 3,
    "C": 3,
    "M": 3,
    "P": 3,
    "F": 4,
    "H": 4,
    "V": 4,
    "W": 4,
    "Y": 4,
    "K": 5,
    "J": 8,
    "X": 8,
    "Q": 10,
    "Z": 10
}

user_input = input("Введите текст: ")

result = 0
for letter in user_input.upper():
    if letter in points.keys():
        result += points[letter]
    else:
        print("Слово использует недопустимые символы!")
        break
else:
    print(f"Ваше слово стоит {result} очков")