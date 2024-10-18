import random

counter = 1
secret = random.randint(1, 10)
print("Хорошо, я загадал число. Попробуй его отгадать")

while 1:
    num = int(input(counter + " "))

    if num == secret:
        print("Поздравляю! Вы угадали!")
        should_continue = input("Хотите продолжить? ")
        if should_continue.lower() == "да":
            secret = random.randint(1, 10)
            print("Хорошо, я загадал число. Попробуй его отгадать")
        else:
            break
    elif num > secret:
       print("Нее, ты не угадал. Попробуй число поменьше")
    else:
       print("Нее, ты не угадал. Попробуй число побольше") 