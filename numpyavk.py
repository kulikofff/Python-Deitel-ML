import numpy as np
'''
numbers = np.array([[2, 3, 5], [4, 5, 6]])
floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])

print(type(numbers))
print(numbers)

print(numbers.dtype)
print(floats.dtype)
print(numbers.ndim)
print(numbers.shape)
print(floats.shape)
print(numbers.size)
print(numbers.itemsize)

for row in numbers:
    for column in row:
        print(column, end=' ')
    print()

for i in numbers.flat:
     print(i, end=' ')
print()
print(np.arange(5)) #arange лучше по времени
print(np.arange(5, 10))
print(np.arange(10, 1, -2))
print(np.linspace(0.0, 1.0, num=5))

a = np.arange(1, 21)
print(a)
a = a.reshape(4, 5)
print(a)
print(a**2)

#print(np.arange(1, 100001).reshape(4, 25000))
# %timeit rolls_array = np.random.randint(1, 7, 6_000_000)

a = np.arange(1, 10, 1)
b = np.arange(21, 30, 1)
print(a)
print(b)
print(a == b)


grades = np.array([[87, 96, 70], [100, 87, 90],
                   [94, 77, 90], [100, 81, 82]])
#print(grades.sum(), grades.min(), grades.max(), grades.mean(), grades.std(), grades.var())
print(grades[0:1])
print(grades[:,2])
print(grades[-2:-1, -2:])
#print(grades.mean(axis=0))

a = np.multiply(grades[0:1], grades[0:1])
print(a)
print(grades[1, 1])
print(grades[2])
print(grades[[1, 3]])
print(grades[:, [0, 2]])

#Поверхностное копирование
numbers = np.arange(1, 6)
numbers[1] *= 10
numbers2 = numbers.view()
numbers3 = numbers[0:3]
print(numbers2, numbers3, id(numbers), id(numbers2), id(numbers3))

#Глубокое копирование
numbers4 = numbers.copy()
print(numbers4)
#Метод resize изменяет размер исходной коллекции array:
'''
grades = np.array([[87, 96, 70], [100, 87, 90],
                   [94, 77, 90], [100, 81, 82]])
#grades.resize(1, 6)

#print(grades)

#Глубокое копирование данных коллекции

#flattened = grades.flatten()
#print(flattened)

#Использование данных

#raveled = grades.ravel()
#print(raveled)

#транспонирование, не изменяет исходную коллекцию array:

#print(grades.T)
#дополнение
grades2 = np.array([[87, 96, 70], [100, 87, 90],
                   [94, 77, 90], [100, 81, 82]])

print(np.hstack((grades, grades2)))

print(np.vstack((grades, grades2)))