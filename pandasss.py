import pandas as pd
'''
grades = pd.Series([87, 100, 94])
print(grades)
print(grades[0])

print(pd.Series(98.6, range(3)))
print(grades.mean())
print(grades.describe())

grades1 = pd.Series([87, 100, 94], index=['Wally', 'Eva', 'Sam'])
print(grades1)

grades2 = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})
print(grades2)
print(grades2['Eva'])
print(grades2.Wally)
print(grades2.dtype)
print(grades2.values)

hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])
print(hardware)

print(hardware.str.contains('a'))
print(hardware.str.upper())
'''

grades_dict = {'Wally': [87, 96, 70], 'Eva': [100, 87, 90],
              'Sam': [94, 77, 90], 'Katie': [100, 81, 82],
              'Bob': [83, 65, 85]}

grades = pd.DataFrame(grades_dict)
print(grades)

pd.DataFrame(grades_dict, index=['Test1', 'Test2', 'Test3'])

grades.index = ['Test1', 'Test2', 'Test3']
print(grades)
print(grades['Eva'])
print(grades.Sam)
print(grades.loc['Test1'])
print(grades.iloc[1])
print(grades.loc['Test1':'Test3'])
print(grades.iloc[0:2])
print(grades.loc[['Test1', 'Test3']])
print(grades.iloc[[0, 2]])
print(grades.loc['Test1':'Test2', ['Eva', 'Katie']])
print(grades.iloc[[0, 2], 0:3])
print(grades[grades >= 90])
print(grades[(grades >= 80) & (grades < 90)]) #and
print(grades[(grades >= 80) | (grades < 90)]) #or
print(grades.at['Test2', 'Eva'])
print(grades.iat[2, 0])
#Присвоение значений
grades.at['Test2', 'Eva'] = 100
print(grades.at['Test2', 'Eva'])
grades.iat[1, 2] = 87
print(grades.iat[1, 2])

#pd.set_option('precision', 2)
print(grades.describe())
print(grades.mean())
print(grades.T)
print(grades.T.describe())
print(grades.sort_index(ascending=False))
print(grades.sort_index(axis=1))
print(grades.sort_values(by='Test1', axis=1, ascending=False))
print(grades.loc['Test1'].sort_values(ascending=False))
#$DataFrame также можно отсортировать на месте, чтобы 
#обойтись без копирования данных. Для этого передайте ключевой аргумент 
#inplace=True функции sort_index или sort_values.