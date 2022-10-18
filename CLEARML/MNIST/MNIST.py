#load model with Joblib - https://clear.ml/docs/latest/docs/guides/frameworks/scikit-learn/sklearn_joblib_example
try:
    import joblib
except ImportError:
    from sklearn.externals import joblib


import pandas as pd
import numpy as np
from clearml import Task
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, ParameterSampler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_auc_score 
from sklearn.datasets import load_digits
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB


###FOR ClearML
task = Task.init(
    project_name='AVT1st', 
    task_name='Cat1', 
    tags=['SKlearn','Digits'])

#Connect to task Clear ML
#task = Task.get_task(task_id='b00931b2346a49dea018c10e8945dd06')

#Dataset
digits = load_digits()
print(digits.DESCR)
print(digits.target[::100])
print(digits.data.shape)
print(digits.target.shape)
print(digits.images[13])
print(digits.data[13])

#Load to ClearML
task.upload_artifact(name='digits', artifact_object=digits)

figure, axes = plt.subplots(nrows=4, ncols=6, figsize=(6, 4))
for item in zip(axes.ravel(), digits.images, digits.target):
     axes, image, target = item
     axes.imshow(image, cmap=plt.cm.gray_r)
     axes.set_xticks([]) # Removing divisions on the x axis
     axes.set_yticks([]) # Removing divisions on the y axis
     axes.set_title(target)
plt.tight_layout()

#Load to ClearML automatically
plt.show()

#Data split
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, random_state=11, test_size=0.24)
print(X_train.shape)
print(X_test.shape)


#Load split Data to ClearML
task.upload_artifact(name='Xdata.train', artifact_object=X_train)
task.upload_artifact(name='Xdata.test', artifact_object=X_test)
task.upload_artifact(name='ydata.train', artifact_object=y_train)
task.upload_artifact(name='ydata.test', artifact_object=y_test)

#ML anl load model in ClearML
knn = KNeighborsClassifier()
knn.fit(X=X_train, y=y_train)
joblib.dump(knn, 'model.pkl', compress=False)
loaded_model = joblib.load('model.pkl')


#Prediction and comparison
predicted = knn.predict(X=X_test)
expected = y_test
print(predicted[:20])
print(expected[:20])
wrong = [(p, e) for (p, e) in zip(predicted, expected) if p != e]
print(wrong)

task.upload_artifact(name='wrong.result', artifact_object=wrong)


#Drawing of a digit
def drawimg(img):
    img=np.reshape(img,(8,8))
    plt.imshow(img)
    plt.show()

image = drawimg(X_test[59])

#Test predict
predictedIMG = knn.predict(X=X_test[59].reshape(1, -1))
print(f'Predicted: {predictedIMG}')
print(f'Real: {y_test[59]}')

#Score
score = knn.score(X_test, y_test)
print(f'Score: {score:.2%}')
task.upload_artifact(name='score', artifact_object=score)

#Confusion Matrix
confusion = confusion_matrix(y_true=expected, y_pred=predicted)
task.upload_artifact(name='confusion', artifact_object=confusion)

#Confusion Matrix visualization
confusion_df = pd.DataFrame(confusion, index=range(10),
    columns=range(10))
axes = sns.heatmap(confusion_df, annot=True,
                    cmap='nipy_spectral_r')
plt.show()


#Metrics
names = [str(digit) for digit in digits.target_names]
metrics = classification_report(expected, predicted, target_names=names)
task.upload_artifact(name='metrics', artifact_object=metrics)

#Cross validation (KFold)
kfold = KFold(n_splits=10, random_state=11, shuffle=True)
scores = cross_val_score(estimator=knn, X=digits.data,
     y=digits.target, cv=kfold)

task.upload_artifact(name='ScoresCrossValidation', artifact_object=scores)

print(f'Mean accuracy CVal: {scores.mean():.2%}')
print(f'Accuracy standard deviation CVal: {scores.std():.2%}')


#Different Estimators
estimators = {
    'KNeighborsClassifier': knn,
    'SVC': SVC(gamma='scale'),
    'GaussianNB': GaussianNB()}

for estimator_name, estimator_object in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scoresdiff = cross_val_score(estimator=estimator_object,
         X=digits.data, y=digits.target, cv=kfold)
    print(f'{estimator_name:>20}: ' +
          f'mean accuracy={scores.mean():.2%}; ' +
          f'standard deviation={scores.std():.2%}')
    task.upload_artifact(name=estimator_name, artifact_object=(estimator_name, scores.mean(), scores.std()))

#Hyperparameters

for k in range(1, 20, 2):
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(estimator=knn,
         X=digits.data, y=digits.target, cv=kfold)
    print(f'k={k:<2}; mean accuracy={scores.mean():.2%}; ' + f'standard deviation={scores.std():.2%}')
    task.upload_artifact(name=(f'K= {k}'), artifact_object=(estimator_name, scores.mean(), scores.std()))

task.close()


