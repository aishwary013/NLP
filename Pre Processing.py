# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 19:15:48 2020

@author: aishwary
"""

import random                              # pseudo-random number generator
import re                                  # library for regular expression operations
import string                              # for string operations
import matplotlib.pyplot as plt            # library for visualization
import nltk                                # Python library for NLP
from nltk.corpus import twitter_samples    # sample Twitter dataset from NLTK
from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.stem import PorterStemmer        # module for stemming
from nltk.tokenize import TweetTokenizer   # module for tokenizing strings

nltk.download('twitter_samples')
nltk.download('stopwords')
stopwords_english = stopwords.words('english') 

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')


# Preprocessing Function
def preprocessing_text(text_list):
    clean_text = []
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,reduce_len=True)
    stemmer = PorterStemmer() 
    for i in range(len(text_list)):
        a = text_list[i]
        a = re.sub(r'^RT[\s]+', '', a)
        a = re.sub(r'https?:\/\/.*[\r\n]*', '', a)
        a = re.sub(r'#', '', a)
        a = tokenizer.tokenize(a)
        a = [item for item in a if item not in stopwords_english]
        a = [item for item in a if item not in string.punctuation]
        a = [stemmer.stem(i) for i in a]
        clean_text.append(a)
    return clean_text

clean_positive_tweets = preprocessing_text(all_positive_tweets)
clean_negative_tweets = preprocessing_text(all_negative_tweets)

