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


#From github
'''
# Сетка для перебора гиперпараметров
param_grid = {
    'depth': [4,5,6,7,8],
    'learning_rate': [0.1,0.05,0.01,0.005,0.001],
    'iterations': [30,50,100,150]
}

# Формируем датасет для тестирования
X_test = test.drop(columns=['Survived'])
y_test = test['Survived']

# Инциируем объект логирования
log = Logger.current_logger()

# Переменные для хранения результатов
best_score = 0
best_model = None
i = 0

# Перебираем случайные 50 гиперпараметров
for param in ParameterSampler(param_grid, n_iter=50, random_state=42):
    # Обучаем модель
    model = CatBoostClassifier(**param, silent=True)
    model.fit(X_train, y_train, cat_features=['Sex','Cabin','Embarked'])

    # Оцениваем модель
    test_scores = model.eval_metrics(
        data=Pool(X_test, y_test, cat_features=['Sex','Cabin','Embarked']),
        metrics=['Logloss','AUC'])
    test_logloss  = round(test_scores['Logloss'][-1], 4)
    test_roc_auc = round(test_scores['AUC'][-1]*100, 1)
    
    train_scores = model.eval_metrics(
        data=Pool(X_train, y_train, cat_features=['Sex','Cabin','Embarked']),
        metrics=['Logloss','AUC'])
    train_logloss  = round(train_scores['Logloss'][-1], 4)
    train_roc_auc = round(train_scores['AUC'][-1]*100, 1)

    # Сравниваем текущий скор с лучшим
    if test_roc_auc > best_score:
        # Сохраняем модель
        best_score = test_roc_auc
        best_model = model

        # Записываем метрики в ClearML
        log.report_scalar("Logloss", "Test", iteration=i, value=test_logloss)
        log.report_scalar("Logloss", "Train", iteration=i, value=train_logloss)
        
        log.report_scalar("ROC AUC", "Test", iteration=i, value=test_roc_auc)
        log.report_scalar("ROC AUC", "Train", iteration=i, value=train_roc_auc)
        
        i+=1

'''

