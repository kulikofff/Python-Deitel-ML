import csv
from pydataset import data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
'''
with open('accounts.csv', mode='w', newline='') as accounts:
     writer = csv.writer(accounts)
     writer.writerow([100, 'Jones, Sue', 24.98])
     writer.writerow([200, 'Doe', 345.67])
     writer.writerow([300, 'White', 0.00])
     writer.writerow([400, 'Stone', -42.16])
     writer.writerow([500, 'Rich', 224.62])

with open('accounts.csv', 'r', newline='') as accounts:
     print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
     reader = csv.reader(accounts)
     for record in reader:
        account, name, balance = record
        print(f'{account:<10}{name:<10}{balance:>10}')


df = pd.read_csv('accounts.csv',
    names=['account', 'name', 'balance'])
print(df)


#Запись скаченного датасета с pydataset в файл как список - заработало с [] в writer.writerow([burt]). Получилась конечно ерунда - в одну ячейку:)
burt = data('Burt')
print(burt)
#print(burt.dtypes)
#docs about dataset
#data('Burt', show_doc=True)
with open('burt.csv', mode='w') as burtfile:
      writer = csv.writer(burtfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
      writer.writerow([burt])


#PLOT

#pd.set_option('precision', 2) # Формат для значений с плавающей точкой, не заработала
burt = data('Burt')
#print(burt.head())
#print()
#print(burt.tail())
burt.columns = ['IQBIO', 'IQFOSTER', 'CLASS']
#print(burt.head())
#print(burt.describe())
#print((burt.CLASS == 'low').describe())

#%matplotlib - не работает
#Можно так выбрать колонки: 
#df = pd.read_excel('https://github.com/datagy/Intro-to-Python/raw/master/sportsdata.xls', usecols=['Age'])

# выбор строк
print(burt[1:5])
# выбор колонок
d = burt.iloc[:, 0:1]
print(d)

d.hist()
burt.hist()
#plt.hist(d['IQBIO'])
plt.show()
'''

burt = data('Burt')
a = [burt[1:2]]
#b = burt[2:3]
print(a)

filename2 = 'items2.csv'

for content in a:  
     list_split = content
               
for content in list_split.items():
          with open(filename2, 'a+', newline='') as f:
               writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
               writer.writerows(content)

print(burt)
#print(b)

#print(burt.__dict__)
#print(burt.__annotations__)
print(len(burt))

for items in burt:  
     list_split = items.split()
     print(list_split)


def user_input_features():
    features = pd.DataFrame(burt, index=[1])
    return features
df = user_input_features()
print(df)

for content in df.items():
          with open(filename2, 'a+', newline='') as f:
               writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
               writer.writerow(content)



#It works - from list to CSV
filename1 = 'items1.csv'
for content in burt.values:
          with open(filename1, 'a+', newline='') as f:
               writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
               writer.writerow(content)
#          print(f'{label}')
#          print(f'{content}', sep='\n')


#filename = 'items.csv'
#for columns in burt:
#     with open(filename, 'a+', newline='') as f:
#          writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#          writer.writerow([columns])
#          writer.writerow([a])
#          writer.writerow([b])

#Graphs
#temps_df = pd.DataFrame(burt, columns=['IQbio', 'IQfoster', 'Class'])
#plt.xlabel('IQbio', color='gray')
#plt.ylabel('IQfoster',color='gray')
#temps_df.plot(x="IQbio", y="IQfoster")
#plt.show()


#grades = pd.Series(burt)
#print(grades[0])

#with open(filename, 'w', newline='') as f:
#            writer = csv.writer(f)
#            for item in burt:
#                writer.writerow([item])

#with open(filename, 'w', newline='') as f:
#            writer = csv.writer(f,delimiter=',')
#            for item in burt:
#                writer.writerows([item])
#                writer.writerow([item])

#with open(filename, 'w', newline='') as f:
#            writer = csv.writer(f)
#            for item in [data('Burt')]:
#                writer.writerow([item])


#Не работает
#data = [data('Burt')]
#np.savetxt(filename, data, delimiter=", ", fmt="% s")