#analyze the AmIA and JAMIA csv files
#aalize the AMia-1981-2021.csv file and the JAMIA-1994-2021.csv file

#import the csv module
import csv
import os
import sys
import re
import datetime
import time
import calendar
import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# import matplotlib.ticker as ticker
# import matplotlib.patches as patches
# import matplotlib.lines as lines
# import matplotlib.text as text
# import matplotlib.image as image
# import matplotlib.colors as colors
import pandas as pd

data = pd.read_csv('C:/Users/admin/Music/Project/AMia-1981-2021.csv')
#comparing two datasets amia and jamia
jamia = pd.read_csv('C:/Users/admin/Music/Project/JAMIA-1994-2021.csv')
amia = pd.read_csv('C:/Users/admin/Music/Project/AMia-1981-2021.csv')

# statistical analisis of the data
print(data.describe())
print(data.head())
print(data.tail())
print(data.info())
print(data.columns)
print(data.dtypes)
print(data.index)
print(data.values)
print(data.shape)
print(data.ndim)
print(data.size)
print(data.memory_usage())
print(data.memory_usage(deep=True))
print(data.memory_usage(index=True, deep=True))
print(data.memory_usage(index=True, deep=True, compute_locations=True))
print(data.memory_usage(index=True, deep=True, compute_locations=True, compute_presence=True))

#data mining and data cleaning
#data mining
#data cleaning

#defining function for tokenization
def tokenize(text):
    return text.split()

#applying function to the column
data['tokenized'] = data['text'].apply(tokenize)

#importing nlp library
import nltk

#Stop words present in the library
stopwords = nltk.corpus.stopwords.words('english')

stopwords[0:10]

#importing the Stemming function from nltk library

# Check distribution of authors in the data
data['author'].value_counts()

# Create word count and character count lists
word_count = []
char_count = []
""""
https://github.com/gkhayes/author_attribution/blob/master/analysis.ipynb

# Create word count and character count lists
# """

for i in range(0, len(authors_information)):
    word_count.append(len(authors_information[i].split()))
    char_count.append(len(authors_information[i]))


