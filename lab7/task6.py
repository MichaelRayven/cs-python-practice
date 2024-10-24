word = input("Введите слово: ")

print(word[0:-1:2] + word[1:-1:2][::-1])