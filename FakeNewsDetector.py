# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 21:55:53 2022

@author: HP
"""
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import stopwords as sp

def textPreProcessing(content):
    stemmed_content = re.sub('ç','c',content)
    stemmed_content = re.sub('[^a-zA-Z]',' ',stemmed_content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    [stemmed_content for word in stemmed_content if not word in sp.STOP_WORDS]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content

dataFrame = pd.read_csv('CSV_news.csv')
dataFrame['lajmi'] = dataFrame['lajmi'].apply(textPreProcessing)


lajmi_values = dataFrame['lajmi'].values
vertetesia_values = dataFrame['vertetesia'].values

vectorizer = TfidfVectorizer()
vectorizer.fit(lajmi_values)

lajmi_values = vectorizer.transform(lajmi_values)

lajmi_train, lajmi_test, vertetesia_train, vertetesia_test = train_test_split(lajmi_values, vertetesia_values, test_size = 0.3, stratify=vertetesia_values, random_state=2)
model = LogisticRegression()

model.fit(lajmi_train, vertetesia_train)

lajmi_train_prediction = model.predict(lajmi_train)
training_data_accuracy = accuracy_score(lajmi_train_prediction, vertetesia_train)

print('Saktesia e te dhenave trajnuese : ', training_data_accuracy)

lajmi_test_prediction = model.predict(lajmi_test)
test_data_accuracy = accuracy_score(lajmi_test_prediction, vertetesia_test)

print('Saktesia e te dhenave testuese : ', test_data_accuracy)

