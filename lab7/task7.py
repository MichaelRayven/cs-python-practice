import random

upper_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_chars = "abcdefghijklmnopqrstuvwxyz"
digit_chars = "1234567890"
special_chars = "!@#$%^&*()_"

length = int(input("Выбирете длину пароля: "))
use_upper = ""
use_lower = ""
use_digits = ""
use_special_chars = ""

while use_upper != "нет" and use_upper != "да":
    use_upper = input("Использовать заглавные буквы (да/нет): ").lower()
else:
    use_upper = use_upper == "да"

while use_lower != "нет" and use_lower != "да":
    use_lower = input("Использовать строчные буквы (да/нет): ").lower()
else:
    use_lower = use_lower == "да"

while use_digits != "нет" and use_digits != "да":
    use_digits = input("Использовать цифры (да/нет): ").lower()
else:
    use_digits = use_digits == "да"

while use_special_chars != "нет" and use_special_chars != "да":
    use_special_chars = input("Использовать специальные символы (да/нет): ").lower()
else:
    use_special_chars = use_special_chars == "да"

choices = upper_chars if use_upper else ""
choices += lower_chars if use_lower else ""
choices += digit_chars if use_digits else ""
choices += special_chars if use_special_chars else ""

if choices == "":
    print("Ошибка: Не выбран ни один тип символов")

password = ""
for i in range(length):
    password += random.choice(choices)

print(f"Пароль длиной {length}: {password}")