
total = 0
age = -1

while age != 0:
    age = int(input(f"Введите возраст посетителя: "))
    if 3 <= age <= 12:
        total += 100
    elif 13 <= age <= 65:
        total += 200
    elif age > 65:
        total += 120

print(f"Итоговая стоймость билетов: {total}")