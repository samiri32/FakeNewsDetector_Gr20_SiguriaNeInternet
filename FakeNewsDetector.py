# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 21:55:53 2022

@author: HP
"""
import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import csv

import nltk 
nltk.download('stopwords')

