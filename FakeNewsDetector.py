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

def textPreProcessing(permbajtja):
    stemmed_content = re.sub('ç','c', permbajtja)
    stemmed_content = re.sub('[^a-zA-Z]',' ', stemmed_content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    [stemmed_content for word in stemmed_content if not word in sp.STOP_WORDS]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content

def print_prediction(vertetesia):
    if vertetesia == 1:
        return "Lajmi është i vërtetë"
    elif vertetesia == 0:
        return "Lajmi nuk është i vërtetë"

def manual_testing(lajmi):
    testing_news = {"teksti":[lajmi]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["teksti"] = new_def_test["teksti"].apply(textPreProcessing) 
    new_x_test = new_def_test["teksti"]
    new_xv_test = vectorizer.transform(new_x_test)
    predikimi = model.predict(new_xv_test)
    return predikimi[0]

dataFrame = pd.read_csv('CSV_news.csv')
dataFrame['lajmi'] = dataFrame['lajmi'].apply(textPreProcessing)


lajmi_values = dataFrame['lajmi'].values
vertetesia_values = dataFrame['vertetesia'].values

vectorizer = TfidfVectorizer()
vectorizer.fit(lajmi_values)

lajmi_values = vectorizer.transform(lajmi_values)

lajmi_train, lajmi_test, vertetesia_train, vertetesia_test = train_test_split(lajmi_values, vertetesia_values, test_size = 0.1, stratify=vertetesia_values, random_state=2)
model = LogisticRegression()

model.fit(lajmi_train, vertetesia_train)

lajmi_train_prediction = model.predict(lajmi_train)
training_data_accuracy = accuracy_score(lajmi_train_prediction, vertetesia_train)

print('Saktesia e te dhenave trajnuese : ', training_data_accuracy)

lajmi_test_prediction = model.predict(lajmi_test)
test_data_accuracy = accuracy_score(lajmi_test_prediction, vertetesia_test)

print('Saktesia e te dhenave testuese : ', test_data_accuracy)

def count_true_predictions():
    dataFrame = pd.read_csv("ScrapAndWriteToCSV.csv")
    count=0
    for i in range(0,dataFrame.shape[0]):
        if manual_testing(dataFrame['lajmi'][i]): count += 1 
    return count,dataFrame.shape[0]

def find_accuarcy_manually():
    return count_true_predictions()[0]/count_true_predictions()[1] #numri i krejt lajmeve t verteta  


