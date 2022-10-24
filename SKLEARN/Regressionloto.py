import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from datetime import datetime
import time
import seaborn as sns
import matplotlib.pyplot as plt

from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train)

lot = pd.read_csv('euromillions-results_ch.csv')

lot.columns = ['Date', 'Numeros', 'Etoiles', 'SUPER-STAR']
#lot.Date = lot.Date.floordiv(100)
print(lot.head(3))
print(lot.dtypes)
#print(lot.shape)

lot["Date"] = [float(str(i).replace(".", "")) for i in lot["Date"]]
lot["Numeros"] = [float(str(i).replace("-", "")) for i in lot["Numeros"]]
lot["Etoiles"] = [float(str(i).replace(".", "")) for i in lot["Etoiles"]]
lot["SUPER-STAR"]=lot["SUPER-STAR"].apply(lambda col:pd.Categorical(col).codes)

print(lot.head(3))
print(lot.dtypes)

#Comment: do not use 'SUPER-STAR' because of letters in it.And also deleted 'Etoiles' 
trg = lot[['Numeros']]
trn = lot.drop(['Numeros','Etoiles','SUPER-STAR'], axis=1)

print(trg.head(3))
print(trn.head(3))


X_train, X_test, y_train, y_test = train_test_split(
    trn.values.reshape(-1, 1),
    trg.values,
    random_state=11)

linear_regression = LinearRegression()
linear_regression.fit(X=X_train, y=y_train)

predicted = linear_regression.predict(X_test)
expected = y_test

for p, e in zip(predicted[::5], expected[::5]):
    print(f'predicted: {p}, expected: {e}')

axes = sns.scatterplot(data=lot, x='Date', y='Numeros',
    hue='Numeros', palette='winter', legend=False)

plt.show()

#print(X_train.shape)
#print(X_test.shape)
#print(y_train.shape)
#print(y_test.shape)
#print(X_train)
#print(y_train)

'''
#Works change of context:
lot["Numeros"] = [float(str(i).replace("-", "")) for i in lot["Numeros"]]
#worked but not for lineregression:
lot['Etoiles'] = pd.to_datetime(lot['Etoiles'].astype(str))
lot['Date'] = pd.to_datetime(lot['Date'].astype(str))
#trn=pd.to_datetime(lot['Date'].astype(str), format='%d.%m.%Y')

#Didn't work:
#trn = pd.Series(trn)
#trn.dt.strftime('%Y-%m-%d')
#x = pd.to_datetime(trn)
#x = trn.transform(lambda x: x + 1)
lot["SUPER-STAR"].apply(lambda x:''.join(['100']+[f'{ord(i):03}' for i in x])).astype(int)
#lot["SUPER-STAR"] = [float(str(i).replace("-", "")) for i in lot["SUPER-STAR"]]
#print(x.value_counts())
#print(trn.dtypes)
#print(trn.describe())
'''

