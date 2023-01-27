# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:01:00 2023

@author: hp
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import pandas as pd

# Load the train data from a CSV file
def load_train_data():
    df = pd.read_csv("fashion-mnist-train-1.csv")
    y = df.iloc[:, 0].values
    X = df.iloc[:, 1:].values
    return X, y

# Load the test data from a CSV file
def load_test_data():
    df = pd.read_csv("fashion-mnist_test.csv")
    y = df.iloc[:, 0].values
    X = df.iloc[:, 1:].values
    return X, y

# Load the train and test data
X_train, y_train = load_train_data()
X_test, y_test = load_test_data()

# Initialize the model
clf = RandomForestClassifier()

# Train the model on the training data
clf.fit(X_train, y_train)

# Evaluate the model on the test data
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print("Accuracy: ", acc)



# save the model
joblib.dump(clf, "model.pkl")
