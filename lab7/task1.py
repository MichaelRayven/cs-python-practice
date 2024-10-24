words = input("Введите предложение: ").split()
new_string = ""

prev = None
for i in range(len(words)):
    if (prev != words[i].lower()):
        new_string += words[i] + " "
        prev = words[i].lower()

print(new_string)