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