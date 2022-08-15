
# Version 1 from AVK
import random, time
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def brosok():
    sum = 0
    for i in range(0,2):
        res = random.randrange(1,7)
        print(f' Result{i} = {res}')
        # Сумма бросков
        sum += res
        print(f' Summ of tries: {sum}')
    return sum

t = int(input('Enter the time for shaking:'))
time.sleep(t)
sum = brosok()
if sum == 7 or sum == 11:
    game_status = 'WON'
    print ('You won!')
elif sum == 2 or sum == 3 or sum == 12:
    game_status = 'LOST'
    print('You lost')
elif sum == 4 or sum == 5 or sum == 6 or sum == 8 or sum == 9 or sum == 10:
    print('You lost, but try again.')
    game_status = 'CONTINUE'

    i = 1
while game_status == 'CONTINUE': 
    t = int(input('Enter the time for shaking:'))
    time.sleep(t)
    print(f' Goal of tries: {sum}')
    sum1 = brosok()
    if sum1 == sum:
        game_status = 'WON'
        print('You won!')
        break
    if sum1 == 7:
        game_status = 'LOST'
        print('You lost')
        break
    else:
        game_status = 'CONTINUE'
        i += 1
        print(f'You lost by {i} attempt')

'''
    
# Version 2 from book
import random

def roll_dice():
    """Моделирует бросок двух кубиков и возвращает результат в виде кортежа."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2) # Два результата упаковываются в кортеж

def display_dice(dice):
    """Выводит результат одного броска двух кубиков."""
    die1, die2 = dice # Распаковывает кортеж в переменные die1 и die2
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')

die_values = roll_dice() # first roll
display_dice(die_values)

# Состояние игры и цель определяются на основании первого броска
sum_of_dice = sum(die_values)


if sum_of_dice in (7, 11): # Выигрыш
    game_status = 'WON'
elif sum_of_dice in (2, 3, 12): # Проигрыш
    game_status = 'LOST'
else: # запомнить цель
    game_status = 'CONTINUE'
    my_point = sum_of_dice
    print('Point is', my_point)

# Броски продолжаются до выигрыша или проигрыша
while game_status == 'CONTINUE':
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)33

    if sum_of_dice == my_point: # Выигрыш по цели
        game_status = 'WON'
    elif sum_of_dice == 7: # Проигрыш по выпадению 7
        game_status = 'LOST'

# Вывод сообщения "wins" или "loses"
if game_status == 'WON':
    print('Player wins')
else:
    print('Player loses')

'''