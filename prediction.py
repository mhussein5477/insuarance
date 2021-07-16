import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


        # using naive bayes to predict from the dataset "insuarance.csv" --------------------
dataset = pd.read_csv("insurance.csv")
replacements = {'no': 0,
                        'yes': 1,
                        'female': 0,
                        'male': 1}
dataset.replace(replacements, inplace=True)
dataset = dataset.astype(float)
dataset[['age', 'sex',  'children']] = dataset[[
            'age', 'sex',  'children']].applymap(np.log)

dataset = dataset.dropna()
x = dataset[['age', 'sex', 'children' ]]
y = dataset['smoker']
x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.2,  random_state=42)
model = GaussianNB()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
accuracy = accuracy_score(y_test, predictions)
print(accuracy)