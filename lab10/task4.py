import os

dir = os.path.dirname(__file__)

number_of_names = int(input("Введите кол-во имен: "))
gender_of_names = input("Введите пол (м/ж): ")

while gender_of_names not in "мж":
    gender_of_names = input("Введите пол (м/ж): ")

if gender_of_names == "м":
    with open(os.path.join(dir, "file8.txt"), "r", encoding="UTF-8") as file:
        for i in range(number_of_names):
            print(f"{file.readline().split()[0]}")
else:
    with open(os.path.join(dir, "file7.txt"), "r", encoding="UTF-8") as file:
        for i in range(number_of_names):
            print(f"{file.readline().split()[0]}")