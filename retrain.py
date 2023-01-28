# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 17:27:21 2023

@author: hp
"""

import argparse
import pandas as pd
from joblib import compat
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score



parser = argparse.ArgumentParser()
parser.add_argument('dataset_name', type=str, help='Name of the dataset to use for training')
args = parser.parse_args()
model = compat.load("model.pkl", mmap_mode='r')

# Read the dataset
df = pd.read_csv(args.dataset_name)

# Split the data into training and testing sets
X = df.iloc[:, 1:].values
y = df.iloc[:, 0].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Retrain the model using the new data
model.fit(X_train, y_train)

# Evaluate the model on the testing set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

joblib.dump(model, "model.pkl")

