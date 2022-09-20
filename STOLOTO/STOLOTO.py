from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
from datetime import datetime
import seaborn as sns
from collections import Counter
import sys

#Take the dataset https://stoloto.vip/5x36 

headers = ['Number','r1', 'r2', 'r3', 'r4', 'r5']
sportloto = pd.read_csv('datasetforpython.csv', sep=';', header=None, names=headers)


for label, content in sportloto.items():
    c = Counter(content)
    print(c)
    minimum = min(c, key=c.get)
    print(f'Minimum: {minimum}')

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
