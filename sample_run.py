import pandas as pd
import string
import re
import seaborn as sns
import warnings
import tensorflow
from tensorflow import keras
from tensorflow.keras import layers, preprocessing, utils  # Updated import
warnings.filterwarnings('ignore')
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from tensorflow.keras.layers import Dense, Input, LSTM, Bidirectional, Activation, Conv1D, GRU  # Updated import
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from tensorflow.keras import models  # Updated import
import pandas as pd 
import numpy as np
import re
import collections
import matplotlib.pyplot as plt
from pathlib import Path
# Packages for data preparation
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from tensorflow.keras.preprocessing.text import Tokenizer  # Updated import
from tensorflow.keras.utils import to_categorical  # Updated import
from sklearn.preprocessing import LabelEncoder
# Packages for modeling
from tensorflow.keras import models, layers, regularizers  # Updated import

#Read Data
df = pd.read_csv('/Users/mcdavid/Desktop/GSU/CSC4810/data.csv')
df
df.info()
df['class'].value_counts() 
df[df['class'] == 'human'].sample(2)
df[df['class'] == 'machine'].sample(2)

df1 = df[0:180000]
df1 = df1.sample(frac=1)
df1

#Text PreprocessingX0 = df1.apply(lambda x: x['Extracted Code'] if x['class'] in ['human','machine']  else x['Extracted Code'], axis = 1)
X0 = df1.apply(lambda x: x['Extracted Code'] if x['class'] in ['human','machine']  else x['Extracted Code'], axis = 1)
X0
X1 = X0
X1
y = df1['class']

#Making Model
x_train, x_test, y_train, y_test = train_test_split(X1,y, random_state=100)
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