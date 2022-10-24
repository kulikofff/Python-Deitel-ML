import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import seaborn as sns
from sklearn import metrics
from sklearn.linear_model import ElasticNet, Lasso, Ridge
from sklearn.model_selection import KFold, cross_val_score

from sklearn.datasets import fetch_california_housing
california = fetch_california_housing()

print('Description:')
print(california.DESCR)
print('Target:')
print(california.target)
print('Features:')
print(california.feature_names)
print()

####Write features to file:
def user_input_features():
    features = pd.DataFrame(california.data, columns=california.feature_names)
    return features
df = user_input_features()

filename1 = 'items1.csv'
for content in df.values:
          with open(filename1, 'a+', newline='') as f:
               writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
               writer.writerow(content)

###Write target to file:
def user_input_features_tar():
    features = pd.DataFrame(california.target, columns=['MedHouseValue'])
    return features
target_df = user_input_features_tar()

filename2 = 'items2.csv'
for content in target_df.values:
          with open(filename2, 'a+', newline='') as f:
               writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
               writer.writerow(content)

###Write all to file:
california_df = pd.DataFrame(california.data,
                            columns=california.feature_names)

#Add a columns from california.target
california_df['MedHouseValue'] = pd.Series(california.target)

filename3 = 'items3.csv'
for content in california_df.values:
          with open(filename3, 'a+', newline='') as f:
               writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
               writer.writerow(content)

###Result
print('Describe Features:')
print(df.head())
print(df.describe())
print()
print('Describe Target:')
print(target_df.head())
print(target_df.describe())
print()
print('Describe Target and Features:')
print(california_df.head())
print(california_df.describe())

'''
#Visualization
sample_df = california_df.sample(frac=0.1, random_state=17)
sns.set(font_scale=2)
sns.set_style('whitegrid')

#data spread charts
for feature in california.feature_names:
    plt.figure(figsize=(16, 9))
    sns.scatterplot(data=sample_df, x=feature,
        y='MedHouseValue', hue='MedHouseValue',
        palette='cool', legend=False)
    plt.show()

'''

X_train, X_test, y_train, y_test = train_test_split(
    california.data, california.target, random_state=11)

print(X_train.shape, X_test.shape)
linear_regression = LinearRegression()
linear_regression.fit(X=X_train, y=y_train)


#Testing model
for i, name in enumerate(california.feature_names):
    print(f'{name:>10}: {linear_regression.coef_[i]}')

print(f' Intercept: {linear_regression.intercept_}')

predicted = linear_regression.predict(X_test)
expected = y_test
print(predicted[:5])
print(expected[:5])
print()

#Testing model with my data
mydata = pd.read_csv("mydata.csv")
print('Mydata:')
print(mydata)
predicted_mydata = linear_regression.predict(mydata)
print('Mydata prediction:')
print(predicted_mydata)

#Expected and Predicted visualization
dff = pd.DataFrame()
dff['Expected'] = pd.Series(expected)
dff['Predicted'] = pd.Series(predicted)

figure = plt.figure(figsize=(9, 9))
axes = sns.scatterplot(data=dff, x='Expected', y='Predicted',
    hue='Predicted', palette='cool', legend=False)
start = min(expected.min(), predicted.min())
end = max(expected.max(), predicted.max())
line = plt.plot([start, end], [start, end], 'k--')
plt.show()

#Metrics
print(f'R2: {metrics.r2_score(expected, predicted)}')
print(f'MSE: {metrics.mean_squared_error(expected, predicted)}')

#Compare better model:
estimators = {
    'LinearRegression': linear_regression,
    'ElasticNet': ElasticNet(),
    'Lasso': Lasso(),
    'Ridge': Ridge()
}
for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator_object,
        X=california.data, y=california.target, cv=kfold,
        scoring='r2')
    print(f'{estimator_name:>16}: ' +
        f'mean of r2 scores={scores.mean():.3f}')