'''
from decimal import Decimal

principal = Decimal('1000.00')
rate = Decimal('0.05')
b = 0

for i in range(1, 100):
    if i == 10:
        break
    else:
        a = principal*(1 + rate) ** i
        b += a
        print(f'{i:>3}{a:>10.2f} sum = {b:>.2f}')
        continue



def square(number):
    """Вычисление квадрата числа."""
    return number ** 2

print(f'{square(2):>10.2f}')
'''

import random
# The same meaning of random initializing
#random.seed(32)

gr1 = 0
gr2 = 0
gr3 = 0
gr4 = 0
gr5 = 0
gr6 = 0
gr7 = 0
gr8 = 0


for i in range(0,1_000_000**1):
    i = random.randrange(1,9)
    if i == 1:
        gr1 += 1
    elif i == 2:
        gr2 += 1
    elif i == 3:
        gr3 += 1        
    elif i == 4:
        gr4 += 1
    elif i == 5:
        gr5 += 1
    elif i == 6:
        gr6 += 1
    elif i == 7:
        gr7 += 1
    elif i == 8:
        gr8 += 1
 
print(f' Gran {"Frequency":>13}') 
print(f' {1:>4}{gr1:>13}') 
print(f' {2:>4}{gr2:>13}') 
print(f' {3:>4}{gr3:>13}') 
print(f' {4:>4}{gr4:>13}') 
print(f' {5:>4}{gr5:>13}') 
print(f' {6:>4}{gr6:>13}') 
print(f' {7:>4}{gr7:>13}') 
print(f' {8:>4}{gr8:>13}') 

print(f'All tries = {sum([gr1, gr2, gr3, gr4, gr5, gr6, gr7, gr8])}')