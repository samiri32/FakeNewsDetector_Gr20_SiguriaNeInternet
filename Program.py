import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import nltk 
nltk.download('stopwords')

print(stopwords.words('albanian'))

news_dataset=pd.read_csv(r"C:\Users\samir\OneDrive\Desktop\ProjektiSiguriNeInternet\faza3\alb-fake-news-corpus\full_texts\fake\1.txt", engine="python")
#print(news_dataset.shape)
print(news_dataset.isnull().sum())

#news_dataset['content']= news_dataset['id']+' '+news_dataset['title']
#print(news_dataset['content'])
