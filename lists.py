'''
c = [-45, 6, 0, 72, 1543]

print(c[0])
print(len(c))
print(c[-1])
c[4] = 'lll'
print(c)
print(c[-1])

s = 'hello'
s[0]
#s[0] = 'H'
#s[6]

print(c[0] + c[1] + c[2])
#print(c[0] + c[1] + c[2] + c[-1])

a_list = []
for i in range(0,7):
    a_list.append(i)

print(a_list)

a_list1 = []
for i in range(0,7):
    a_list1 += [i]

print(a_list1)

letters = []
letters += 'Python'
print(letters)


a = ('p', 'y', 't', 'h', 'o', 'n')
#кортеж в список
letters1 = []
letters1 += a
print(letters1)

for i in range(len(letters1)):
    print(letters1[i])

# кортеж неизменяем
#a[0] = 'pp'

# список в кортеже изменяем
student_tuple = ('Amanda', 'Blue', [98, 75, 87])

student_tuple[2][1] = 85
print(student_tuple)

number1, number2, number3 = range(50, 20, -10)
print(f'{number1} {number2} {number3}')

colors = ['red', 'orange', 'yellow']
print(list(enumerate(colors)))
print(tuple(enumerate(colors)))

for index, value in enumerate(colors):
    print(f'{index}: {value}')


numbers = [19, 3, 15, 7, 11]
print(f'Index{"Value":>8} Bar')
for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8} {"*" * value}')

#пошагово
print(numbers[::-1])

numbers1 = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6, 5, 5, 5]
print(sorted(numbers1))

print(numbers1.index(4, 0))

#Трансформация списка, аналог for:

list2 = [item for item in range(1, 6)]
print(list2)

list3 = list(range(1, 6))
print(list3)

list4 = [item for item in range(1, 11) if item % 2 == 0]
print(list4)

colors = ['red', 'orange', 'yellow', 'green', 'blue']
colors2 = [i.upper() for i in colors]
print(colors2)

# Выражения-генераторы, не создает список, в круглых скобках
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
for value in (x ** 2 for x in numbers if x % 2 != 0):
    print(value, end=' ')

numbers1 = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
def is_odd(x):
    """Возвращает True только для нечетных x."""
    return x % 2 != 0

print(list(filter(is_odd, numbers1)))

print([item for item in numbers1 if is_odd(item)])

print(list(filter(lambda x: x % 2 != 0, numbers1)))

#Отличия:
# def имя_функции(список_параметров):
#return выражение

#lambda список_параметров: выражение

print(list(map(lambda x: x ** 2, numbers1)))
print([item ** 2 for item in numbers1])

print(list(map(lambda x: x ** 2,
    filter(lambda x: x % 2 != 0, numbers1))))
print([x ** 2 for x in numbers1 if x % 2 != 0])
'''
#в алфавитный порядок
colors = ['Red', 'orange', 'Yellow', 'green', 'Blue']
print(min(colors, key=lambda s: s.lower()))
print(max(colors, key=lambda s: s.lower()))

#Обратный перебор элементов последовательности
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]
print([item for item in reversed(numbers)])

#Объединение итерируемых объектов в кортежи с соответствующими элементами
names = ['Bob', 'Sue', 'Amanda']
grade_point_averages = [3.5, 4.0, 3.75]
for name, gpa in zip(names, grade_point_averages):
    print(f'Name={name}; GPA={gpa}')

#Двумерный список
a = [[77, 68, 86, 73], [96, 87, 89, 81], [70, 90, 86, 81]]

print(a[2][3])

for row in a:
    for item in row:
        print(item, end=' ')
    print()

for i, row in enumerate(a):
    for j, item in enumerate(row):
        print(f'a[{i}][{j}]={item} ', end=' ')
    print()