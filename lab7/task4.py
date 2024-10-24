sentence = input("Введите предложение: ")

sentence = sentence.replace("не плохой", "хороший")
sentence = sentence.replace("не плоха", "хороша")

sentence = sentence.replace("Не плохой", "Хороший")
sentence = sentence.replace("Не плоха", "Хороша")

print(sentence)