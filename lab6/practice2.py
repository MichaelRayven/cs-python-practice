visitors_count = int(input("Количество поситителей: "))
total = 0

for i in range(visitors_count):
    age = int(input(f"Введите возраст {i+1}-го посетителя: "))
    if 3 <= age <= 12:
        total += 100
    elif 13 <= age <= 65:
        total += 200
    elif age > 65:
        total += 120

print(f"Итоговая стоймость билетов: {total}")