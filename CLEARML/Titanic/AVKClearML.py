import pandas as pd
import numpy as np
from clearml import Task, Logger
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, ParameterSampler
from catboost import CatBoostClassifier, Pool
from sklearn.metrics import roc_auc_score 

task = Task.init(
    project_name='AVT1st', 
    task_name='Cat1', 
    tags=['CatBoost','RandomSearch'])

#Connect to task
prev_task = Task.get_task(task_id='0466c2c95b38451eafc052a7a4e7c31f')

fpath = 'titanic.csv'
df_raw = pd.read_csv(fpath)
task.upload_artifact(name='data.raw', artifact_object=fpath)


task.upload_artifact(
    name='eda.describe.object', 
    artifact_object=df_raw.describe(include=object))
task.upload_artifact(
    name='eda.describe.number', 
    artifact_object=df_raw.describe(include=np.number))

sns.pairplot(df_raw, hue='Survived')
plt.title('Pairplot')
plt.show()


#Dataset
df_preproc = df_raw.drop(columns=['PassengerId','Name','Ticket', 'Pclass'])


for col in ['Sex','Cabin','Embarked']:
    df_preproc[col] = df_preproc[col].astype(str)
task.upload_artifact(name='data.preproc', artifact_object=df_preproc)

train, test = train_test_split(df_preproc, test_size=0.33, random_state=42)
task.upload_artifact(name='data.train', artifact_object=train)
task.upload_artifact(name='data.test', artifact_object=test)


#Train
X = train.drop(columns=['Survived'])
y = train['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.45, random_state=42)

#First
#model = CatBoostClassifier(silent=True)
#model.fit(X_train, y_train, cat_features=['Sex','Cabin','Embarked']);

#Experiment
model1 = CatBoostClassifier(
    learning_rate=0.7,
    iterations=200,
    random_seed=63,
    custom_loss=['AUC', 'Accuracy']
)
model1.fit(X_train, y_train, cat_features=['Sex','Cabin','Embarked'], eval_set=(X_test, y_test), verbose=35, plot=True)

model2 = CatBoostClassifier(
    learning_rate=0.01,
    iterations=200,
    random_seed=63,
    custom_loss=['AUC', 'Accuracy']
)
model2.fit(X_train, y_train, cat_features=['Sex','Cabin','Embarked'], eval_set=(X_test, y_test), verbose=35, plot=True)


model1.save_model('my_model1.cbm')
model2.save_model('my_model2.cbm')
task.close()

