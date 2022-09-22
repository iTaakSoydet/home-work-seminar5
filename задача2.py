""" 2.Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом"" """

""" from random import randint
candies = 2021
print(f'{candies} всего конфет')
count = randint(1, 2)
while candies > 0:
    count += 1
    if count % 2 == 0:
        print('ходит игрок 2')
    else:
        print('ходит игрок 1')
    quantity = int(input('Введите число конфет которое изымаете - '))
    if 0 < quantity < 29:
        candies -= quantity
        print(f'конфет осталось - {candies}')
    else:
        print('Вы ввели некоректное кол-во конфет, введите число от 1 до 28')
        count -=1

if count % 2 == 0:
    print('победил игрок 2')
else:
    print('победил игрок 1') """

""" # А) 

candies = 2021
print(f'{candies} всего конфет')
count = randint(1, 2)
while candies > 0:
    count += 1
    if count % 2 == 0:
        print('ходит бот')
        quantity = randint(1, 28)
        print(f'конфет изымаете бот {quantity}')
    else:
        print('ходит игрок')
        quantity = int(input('Введите число конфет которое изымаете - '))
    if 0 < quantity < 29:
        candies -= quantity
        print(f'конфет осталось - {candies}')
    else:
        print('Вы ввели некоректное кол-во конфет, введите число от 1 до 28')
        count -=1

if count % 2 == 0:
    print('победил бот')
else:
    print('победил игрок') """

# Б)

candies = 2021
print(f'{candies} всего конфет')
count = randint(1, 2)
while candies > 0:
    count += 1
    if count % 2 == 0:
        if count == 2:
            print('ходит бот')
            quantity = 20
            print(f'конфет изымаете бот {quantity}')
        else:
            print('ходит бот')
            quantity = 29 - quantity
            print(f'конфет изымаете бот {quantity}')
    else:
        print('ходит игрок')
        quantity = int(input('Введите число конфет которое изымаете - '))
    if 0 < quantity < 29:
        candies -= quantity
        print(f'конфет осталось - {candies}')
    else:
        print('Вы ввели некоректное кол-во конфет, введите число от 1 до 28')
        count -= 1

if count % 2 == 0:
    print('победил бот')
else:
    print('победил игрок')
