num = input()

if len(num) == 6:
    first_half_sum = 0
    second_half_sum = 0
    for i in range(3):
        first_half_sum += int(num[i])
        second_half_sum += int(num[len(num) - 1 - i])
        
    if first_half_sum == second_half_sum:
        print("Поздравляю! Ваш билет - счастливый")
    else:
        print("Обычный билет")
else:
    print("Некорректный билет")

