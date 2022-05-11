# -*- coding: utf-8 -*-
"""MachineLearningProject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gru-QYXhJ_ff-Q6kz8PjwZrvoSBOJ78t

# Installation
"""

#Import pandas library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""# Importing the Dataset"""

df = pd.read_csv('https://drive.google.com/uc?id=10u_8dlMO7Dh4oeggUVp6pbZ2cvCzIWaZ')


#Now print the first few rows and last few rows of the imported dataframe
print(df.head(10))
print(df.tail(10))


#Print and view the columns that our DataFrame contains
print(df.columns)

"""The dataset we have selected is from the following URL **[Dataset](https://www.kaggle.com/rashikrahmanpritom/heart-attack-analysis-prediction-dataset)** and the link contains a brief desciption of the CSV headers.</br></br>
The aim is to predict based on the input parameters if a person is prone to Heart Attacks based on the dataset collected using **Binary Classification** and to compare the various types of classification and find the best one for our data
"""

#Check for null values
if df.isnull().values.sum()==0:
    print(f'Sum = {df.isnull().values.sum()}')
    print(f'{df.isnull()}')
    print("No Null values in DataFrame")
else:
    print('Move on and Clean the DataFrame using Pandas')

"""Since there are no NULL values we can carry on to perform the Classification

We will use the following methods

1. **Logistic Regression**
2. **Naive Baye's Classifier**
3. **K-Nearest Neighbors**
4. **Decision Tree**
3. **Support Vector Machines**

Visualise the results
"""

def visualise_cm(classifier, X_test, y_test):
  from sklearn.metrics import plot_confusion_matrix
  plot_confusion_matrix(classifier, X_test, y_test) 
  plt.show()

plt.rc_context({'axes.edgecolor':'#581845', 'xtick.color':'black', 'ytick.color':'black', 'figure.facecolor':'#f6eee2', 'font.family' : 'serif', 'figure.figsize': "15, 10", 'font.size': "22"})

result = []

"""Dependent and Independent Variables"""

X = df.iloc[:, :-1].values
y = df.iloc[:, -1:].values

"""Train - Test Split"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

"""Feature Scaling

"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""# Logistic Regression

Training the model
"""

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train.ravel())

"""Prediction and Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
result.append(accuracy_score(y_test, y_pred))
accuracy_score(y_test, y_pred)

visualise_cm(classifier, X_test, y_test)

"""# Naive Baye's

Training the Naive Bayes Classifier on Train set
"""

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train.ravel())

"""Predicting the Test set results"""

y_pred = classifier.predict(X_test)

"""Calculating the Accuracy"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
result.append(accuracy_score(y_test, y_pred))
accuracy_score(y_test, y_pred)

visualise_cm(classifier, X_test, y_test)

"""# KNN

Finding the optimal k value
"""

# Optimal K value would be sqrt(N) where N is the number of samples in training dataset  
N = len(X_train)
print(N)
k = int(N**0.5)

"""Training the K-Nearest Neighbors Classifier on Train set


"""

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=k)
classifier.fit(X_train, y_train.ravel())

"""Predicting the test set Results"""

y_pred = classifier.predict(X_test)

"""Calculating the Accuracy"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
result.append(accuracy_score(y_test, y_pred))
accuracy_score(y_test, y_pred)

visualise_cm(classifier, X_test, y_test)

"""# Decision Tree

Training the Decision Tree Classifier on Train set
"""

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier()
classifier.fit(X_train, y_train)

"""Predicting the test set Results"""

y_pred = classifier.predict(X_test)

"""Calculating the Accuracy"""

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)

result.append(accuracy_score(y_test, y_pred))
accuracy_score(y_test, y_pred)

visualise_cm(classifier, X_test, y_test)

"""# SVM

Check if the Linear Kernel is working well
"""

from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
#Check if the Linear Kernel is working well
classifier = SVC(kernel='linear')
classifier.fit(X_train, y_train.ravel())


y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
result.append(accuracy_score(y_test, y_pred))
accuracy_score(y_test, y_pred)

visualise_cm(classifier, X_test, y_test)

"""Check if the Radial Kernel is working well"""

#Check if the Radial Kernel is working well
classifier = SVC(kernel='rbf')
classifier.fit(X_train, y_train.ravel())


y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
result.append(accuracy_score(y_test, y_pred))

accuracy_score(y_test, y_pred)

visualise_cm(classifier, X_test, y_test)

"""Check if the Polynomial Kernel is working well"""

#Check if the Polynomial Kernel is working well
classifier = SVC(kernel='poly')
classifier.fit(X_train, y_train.ravel())


y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
result.append(accuracy_score(y_test, y_pred))

accuracy_score(y_test, y_pred)

visualise_cm(classifier, X_test, y_test)

"""Check if the Sigmoid Kernel is working well"""

#Check if the Sigmoid Kernel is working well
classifier = SVC(kernel='sigmoid')
classifier.fit(X_train, y_train.ravel())


y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
result.append(accuracy_score(y_test, y_pred))
accuracy_score(y_test, y_pred)

visualise_cm(classifier, X_test, y_test)

"""# Conclusion"""

models = ['Logistic', 'Naive Bayes','KNN','Decision Tree', 'Linear SVM','Radial SVM']
plt.bar(models, result[:6])
plt.xlabel("Models")
plt.ylabel("Accuracies")
plt.show()

