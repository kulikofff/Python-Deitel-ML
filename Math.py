'''
import math

math.sqrt(900)
math.fabs(-10)
math.floor(9.2)
print(math.e)
print(math.pi)

def rectangle_area(length=2, width=3):
    """Возвращает площадь прямоугольника."""
    return length * width

print(rectangle_area())
print(rectangle_area(4,4))
print(rectangle_area(4))

def average(*args):
    return sum(args) / len(args)

grades = [88, 75, 96, 55, 83]
print(average(*grades))
#* - распаковка элементов кортежа


s = 'Hello'
print(s.lower())

x = 'bye'
def modify_global():
     global x
     x = 'hello'
     print('x printed from modify_global:', x)

modify_global()
print(x)

sum = 10 + 5
print(sum)

# замещение функций
sum([10,5])


import statistics
from statistics import mean as m

grades = [85, 93, 45, 87, 93]

print(m(grades))

print(id(grades))

x = 7
def cube(number):
    print('number is x:', number is x) # x - глобальная переменная
    return number ** 3

print(cube(x))
'''

factorial = 1
for number in range(5, 0, -1):
    factorial *= number

print(factorial)

# Рекурсие (разбиение на мелкие части)

def factorial(number):
#"""Возвращает факториал числа."""
    if number <= 1:
        return 1
    return number * factorial(number - 1) # Рекурсивный вызов

for i in range(11):
    print(f'{i}! = {factorial(i)}')


import statistics

# Дисперсия
print(statistics.pvariance([1, 3, 4, 2, 6, 5, 3, 4, 5, 2]))

# Ср.кв.отклонение = кореннь из дисперсии
print(statistics.pstdev([1, 3, 4, 2, 6, 5, 3, 4, 5, 2]))