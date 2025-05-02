import pandas as pd
import string
import re
import seaborn as sns
import warnings
import tensorflow
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import collections
from tensorflow import keras
from tensorflow.keras import models, layers, preprocessing, utils, regularizers
warnings.filterwarnings('ignore')
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from tensorflow.keras.layers import Dense, Input, LSTM, Bidirectional, Activation, Conv1D, GRU
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from tensorflow.keras import models 
from pathlib import Path
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.text import Tokenizer 
from tensorflow.keras.utils import to_categorical 
from sklearn.preprocessing import LabelEncoder

#Read Data
df = pd.read_csv('/Users/mcdavid/Desktop/GSU/CSC4810/cleaned_data.csv')
df
df.info()
print(df.head())


df['class'].value_counts() 
df[df['class'] == 'human'].sample(2)
df[df['class'] == 'machine'].sample(2)

print(len(df))
df1 = df[:]

df1 = df1.sample(frac=0.8, random_state=42)  


#Data Cleaning
X0 = df1['Extracted Code']
X1 = X0
y = df1['class']

#Making Model
x_train, x_test, y_train, y_test = train_test_split(X1,y,train_size=0.8, random_state=100)
vectorizer = TfidfVectorizer(ngram_range=(1,5), analyzer='char')
model = pipeline.Pipeline([
    ('vectorizer', vectorizer),
    ('clf', LogisticRegression())
])
model.fit(x_train, y_train)



#Checking for Accuracy
y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

print("Accuracy is :",accuracy)
print("Confusion Matrix:\n", cm)
print("Classification Report:\n", classification_report(y_test, y_pred))


# Plotting the confusion matrix
import matplotlib.pyplot as plt
plt.figure(figsize=(15,10))
sns.heatmap(cm, annot = True)
plt.show()


#Testing Model
def predict(text):
    lang = model.predict([text])
    print(text)
    print('this code is written by: ',lang[0])
    print("######################")

alist = df1['Extracted Code'].sample(n=10, random_state=2)
for i in alist:
    predict(i)