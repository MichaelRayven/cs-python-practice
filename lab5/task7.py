num = input("Введите номерной знак: ")

# Old AAA000
# New 0000AAA

is_correct = False

if len(num) == 6:
    is_old = num[0:3].isupper() and num[-3:].isdigit()
    if is_old:
        is_correct = True
        print("Старый формат")
elif len(num) == 7:
    is_new = num[0:4].isdigit() and num[-3:].isupper()
    if is_new:
        is_correct = True
        print("Новый формат")

if not is_correct:
    print("Не соответствует формату")