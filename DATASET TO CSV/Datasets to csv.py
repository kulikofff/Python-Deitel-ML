import pandas as pd
import csv
from sklearn.datasets import fetch_california_housing
from pydataset import data


### DATASET 1 ###
california = fetch_california_housing()

print('Type of dataset:')
print(type(california))
print()
#It's a bunch - https://scikit-learn.org/stable/modules/generated/sklearn.utils.Bunch.html
#Bunch objects are sometimes used as an output for functions and methods. 
#They extend dictionaries by enabling values to be accessed by key, bunch["value_key"], or by an attribute, bunch.value_key.
#A Bunch is a subclass of dict; it supports all the methods a dict does:

print('Input dataset:')
print(california)
print()
print('Description:')
print(california.DESCR)
print()
print('Target_name:')
print(california.target_names)
print()
print('Target:')
print(california.target)
print()
print('Features:')
print(california.feature_names)
print()
print('Head:')
print(california.data)
print()
print('Items:')
print()
print(california.items())
print()
print('Values:')
print()
print(california.values())


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

### DATASET 2 ###

burt = data('Burt')
print()
print('Type of dataset:')
print(type(burt))
print()
print('Burt Dataset:')
print(burt)

filename4 = 'items4.csv'
for content in burt.values:
          with open(filename4, 'a+', newline='') as f:
               writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
               writer.writerow(content)


