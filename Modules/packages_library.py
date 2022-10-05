import numpy as np
import pandas as pd
import pingouin as pg
import os
import datetime
import time
import spacy

import itertools
from collections import Counter
import re

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.legend import Legend
from matplotlib.gridspec import GridSpec
import seaborn as sns

import scipy.stats as stats

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import words
from nltk import SnowballStemmer
from nltk import ngrams

from os import listdir
from os.path import isfile, isdir

wordnet_lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('spanish')) # Remove useless words
#stop_words.update(newStopWords)
spanishstemmer = SnowballStemmer('spanish')

import warnings

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import RandomizedSearchCV