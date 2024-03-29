#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: stleroux
"""

# Project guided by Daniel Romaniuk

# Import necessary packages for decision tree analysis
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy score
from sklearn.mertrics import classification_report
from sklearn import tree

# Attribute names here
att_names = ('age', 'workclass', 'fnlwgt', education', 'education-num', 'marital-status',
'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hrs-per-week',
'native-country', 'salary-class')

# Read the CSV file, downloaded onto computer
# Specifying Python engine as initally written in Jupyter
data = pd.read_csv('adult.data', names=att_names, sep=', ', engine='python')

# Preprocessing data
excludes = ('fnlwgt', 'education-num', 'capital-gain', 'capital-loss')
for att in excludes:
  del data[att]

# Creating indicator variables
boolean = ('sex', 'native-country', 'salary-class')
for att in boolean:
  data[att] = data[att].astype('category')
  data[att] = data[att].cat.codes

# Encoding of categorical vars
categoricals = ('workclass', 'education', 'marital-status', 'occupation', 'relationship',
'race')
for att in categoricals:
  data = pd.concat([data, pd.get_dummies(data[att], prefix=att)], axis=1)
  del data[att] #Update the df

# Extract attributes and class labels; x and y respectively
y = data['salary-class']
X = data.copy().drop(columns='salary-class')

#train-test split
X_train, X_test, y_train, y_test = train_test_split(
  X,
  y,
  test_size=0.33,
  random_state=1
)

# I promise I unit test in Jupyter... excuse my lack of print statements :D
# Here is a print statement to test the size-shape of the model

print('X_train ', X_train.shape)
print('X_test: ' X_test.shape)
print('y_train: ' y_train.shape)
print('y_test: ' y_test.shape)

# Constructing a decision tree from this training data
clf = DecisionTreeClassifier(random_state=0, criterion='entropy')
clf.fit(X_train, y_train)

# Predict target class test/train
y_train_pred = clf.predict(X_train)
train_acc = accuracy_score(y_train, y_train_pred)
print("Train: ", train_acc) #0.97137

y_train_pred = clf.predict(X_test)
train_acc = accuracy_score(y_test, y_test_pred)
print("Test: ", test_acc) #0.77871

#pruning the decision tree
#once again, trust me the dataset was assessed for balance ;) 

sizes = [2, 3, 5, 10, 20, 50, 100, 250, 750, 1000, 2500, 5000, 10000, 15000]
for size in sizes:
  clf = DecisionTreeClassifier(random_state=0, criterion='entropy', min_samples_split=s)
  clf.fit(X_train, y_train)

  y_train_pred = clf.predict(X_train)
  train_acc = accuracy_score(y_train, y_train_pred)

  y_train_pred = clf.predict(X_test)
  train_acc = accuracy_score(y_test, y_test_pred)

  train_accs.append(train_acc)
  test_accs.append(test_acc)

plt.plot(sizes) #plotting train/test set while 

fig = plt.figure(figsize=(40,40))
p = tree.plot_tree(clf, filled=True, feature_names=X_train.columns.to_list(), class_names=("low", "high"))
fig.savefig("natureiscool.png") 
