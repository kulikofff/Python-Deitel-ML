#ipython --matplotlib

import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
from datetime import datetime
import seaborn as sns
from collections import Counter

#Example - works
'''
c = lambda f: 5 / 9 * (f - 32)
temps = [(f, c(f)) for f in range(0, 101, 10)]

temps_df = pd.DataFrame(temps, columns=['Fahrenheit', 'Celsius'])
#axes = plt.temps_df.plot(x='Fahrenheit', y='Celsius', style='.-')
#y_label = axes.set_ylabel('Celsius')


plt.xlabel('Fahrenheit', color='gray')
plt.ylabel('Celsius',color='gray')

plt.plot(temps)
temps_df.plot(x="Fahrenheit", y="Celsius")

plt.show()
'''

#print(sportloto.tail())
#print(sportloto.Date.dtype)
#print(sportloto.info())
#print(sportloto['Date'].max())
#print(sportloto['Date'].min())

#It works:)
#plt.xlabel('r1', color='gray')
#plt.ylabel('Date',color='gray')
#plt.plot(sportloto)
#sportloto.plot(x="r1", y="Date")
#sportloto.plot(x="Date", y="r1")
#plt.show()

#print(sportloto.Date.describe())
#print(sportloto.r1.describe())

#Предсказание результата следующего тиража:
#print(linear_regression.slope)
#print(linear_regression.intercept)



#Seaborn for points
#sns.set_style('whitegrid')
#axes = sns.regplot(x=sportloto.Number, y=sportloto.r1)
#axes.set_ylim(0, 40)
#axes.set_xlim(1, 200)
#plt.show()

#Seaborn with date
#sns.scatterplot(data=sportloto, x="Date", y="r1")
#plt.show()
#sns.lineplot(data=sportloto, x="Date", y="r1")
#plt.show()
#Loadiong long
#sns.barplot(data=sportloto, x="Date", y="r1")
#plt.show()

# Не имело эффекта
#sportloto['Date'] = pd.to_datetime(sportloto['Date'], format='%d-%m-%y')
#print(sportloto.head())
#print(sportloto['r1'].count())

#https://stoloto.vip/5x36 
#headers = ['Number','Date','r1', 'r2', 'r3', 'r4', 'r5']
headers = ['Number','r1', 'r2', 'r3', 'r4', 'r5']
#Изменение типа данных в Date
#sportloto = pd.read_csv('./STOLOTO/5from36forecastfullv1.csv', sep=',', header=None, names=headers, parse_dates=['Date'])
#Data from 15092022
sportloto = pd.read_csv('./STOLOTO/newarchiv5iz36150920221703.csv', sep=';', header=None, names=headers)


for label, content in sportloto.items():
    c = Counter(content)
    print(Counter(content))
    minimum = min(c, key=c.get)
    print(f'Minimum: {minimum}')
#    print(f'label: {label}')
#    print(f'content: {content}', sep='\n')

for label, content in sportloto.items():
    d = Counter(content)
    maximum = max(d, key=d.get)
    print(f'Maximum: {maximum}')


plt.subplot(1, 5, 1)
sns.countplot(x='r1', data=sportloto)
plt.subplot(1, 5, 2)
sns.countplot(x='r2', data=sportloto)
plt.subplot(1, 5, 3)
sns.countplot(x='r3', data=sportloto)
plt.subplot(1, 5, 4)
sns.countplot(x='r4', data=sportloto)
plt.subplot(1, 5, 5)
sns.countplot(x='r5', data=sportloto)
plt.show()



#Предсказание по будущему номеру. Но всегда будет 16
linear_regression1 = stats.linregress(x=sportloto.Number, y=sportloto.r1)
print(linear_regression1.slope * 53108 + linear_regression1.intercept)

linear_regression2 = stats.linregress(x=sportloto.Number, y=sportloto.r2)
print(linear_regression2.slope * 53108 + linear_regression2.intercept)

linear_regression3 = stats.linregress(x=sportloto.Number, y=sportloto.r3)
print(linear_regression3.slope * 53108 + linear_regression3.intercept)

linear_regression4 = stats.linregress(x=sportloto.Number, y=sportloto.r4)
print(linear_regression4.slope * 53108 + linear_regression4.intercept)

linear_regression5 = stats.linregress(x=sportloto.Number, y=sportloto.r5)
print(linear_regression5.slope * 53108 + linear_regression5.intercept)

print(linear_regression1.slope, linear_regression2.slope, linear_regression3.slope, linear_regression4.slope, linear_regression5.slope)
print(linear_regression1.intercept, linear_regression2.intercept, linear_regression3.intercept, linear_regression4.intercept, linear_regression5.intercept)
