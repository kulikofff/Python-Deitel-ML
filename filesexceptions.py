import os
import json
'''
with open('accounts.txt', mode='w') as accounts:
    accounts.write('100 Jones 24.98\n')
    accounts.write('200 Doe 345.67\n')
    accounts.write('300 White 0.00\n')
    accounts.write('400 Stone -42.16\n')
    accounts.write('500 Rich 224.62\n')

with open('accounts1.txt', mode='w') as accounts1:
     print('100 Jones 24.98', file=accounts1)



with open('accounts.txt', mode='r') as accounts:
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    for record in accounts:
        account, name, balance = record.split()
        print(f'{account:<10}{name:<10}{balance:>10}')

with open('accounts.txt', mode='r') as accounts:
    print(accounts.seek(0))


accounts = open('accounts.txt', 'r')
temp_file = open('temp_file.txt', 'w')
with accounts, temp_file:
    for record in accounts:
        account, name, balance = record.split()
        if account != '300':
            temp_file.write(record)
        else:
            new_record = ' '.join([account, 'Williams', balance])
            temp_file.write(new_record + '\n')

os.remove('accounts.txt')
os.rename('temp_file.txt', 'accounts.txt')

#JSON

accounts_dict = {'accounts': [
    {'account': 100, 'name': 'Jones', 'balance': 24.98},
    {'account': 200, 'name': 'Doe', 'balance': 345.67}]}


with open('accounts.json', 'w') as accounts:
    json.dump(accounts_dict, accounts)

with open('accounts.json', 'r') as accounts:
    accounts_json = json.load(accounts)

print(accounts_json, accounts_json['accounts'])

#!!!!
print(accounts_json['accounts'][0], accounts_json['accounts'][1])

#indent
with open('accounts.json', 'r') as accounts:
     print(json.dumps(json.load(accounts), indent=4))
'''

while True:
 # Пытаемся преобразовать и разделить значения
    try:
        number1 = int(input('Enter numerator: '))
        number2 = int(input('Enter denominator: '))
        result = number1 / number2
    except ValueError: # Попытка преобразования в int некорректного значения
        print('You must enter two integers\n')
    except ZeroDivisionError: # Делитель равен 0
        print('Attempted to divide by zero\n')
    else: # Выполняется только при отсутствии исключений
        print(f'{number1:.3f} / {number2:.3f} = {result:.3f}')
    break # завершает цикл

def function1():
    function2()

def function2():
    raise Exception('An exception occurred')

print(function1())