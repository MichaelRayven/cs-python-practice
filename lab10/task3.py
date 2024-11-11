import os

dir = os.path.dirname(__file__)



with open(os.path.join(dir, "file6.txt"), "r", encoding="utf8") as file:
    count_with_e = 0
    count = 0
    for line in file.readlines():
        for word in line.split():
            if "e" in word.lower():
                count_with_e += 1
            count += 1

print(f"Всего слов: {count}, слов с буквой `e`: {count_with_e}, процент: {count_with_e/count*100:.2f}%")