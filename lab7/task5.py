lines = input("Введите предложение: ").split("/")

if len(lines) != 3:
    print("Не хайку. Должно быть 3 строки.")
else:
    for i in range(len(lines)):
        count_vowels = 0
        for char in lines[i]:
            if char in "aeiouAEIOUауоиэыяюеёАУОИЭЫЯЮЕЁ":
                count_vowels += 1

        if (i % 2 == 0):
            if count_vowels != 5:
                print("Не хайку.")
                break
        else:
            if count_vowels != 7:
                print("Не хайку.")
                break
    else:
        print("Хайку!")

