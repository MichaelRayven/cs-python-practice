years = int(input())

if years > 2:
    print(f"Введенный вами год эквивалентен {21 + (years - 2) * 4} человеческим")
elif years > 0:
    print(f"Введенный вами год эквивалентен {10.5 * years} человеческим")
else:
    print("Ошибка!")