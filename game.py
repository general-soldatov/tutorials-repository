import random

UnknowNumber = random.randint(1,30)

EnterNumber = -1

while EnterNumber != UnknowNumber:
    EnterNumber = int(input('Введите числе от 1 до 30: '))
    if EnterNumber < UnknowNumber:
        print("Введёное число меньше искомого")
    elif EnterNumber > UnknowNumber:
        print("Введёное число больше искомого")
    elif EnterNumber == UnknowNumber:
        print("Ты угадал, поздравляю!")