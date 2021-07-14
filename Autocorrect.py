# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 18:34:48 2020

@author: aishwary
"""

from os import chdir
chdir(r'G:\My Drive\2020\Coding\NLP\NLP with Probabilistic Models')
import re


# Read a file and store distinct words in a list
def process_text(file_name):
    words = []
    with open(file_name) as f:
        read_data = f.read()
        read_data = read_data.lower()
        words = re.findall('\w+', read_data, flags=0)
    return words

words = process_text('check.txt')
    
# Get count of individual words in a dictionary
def get_count(word_list):
    words_count_dict = {}
    for i in set(word_list):
        words_count_dict[i]=0
    for i in word_list:
        words_count_dict[i] = words_count_dict.get(i) + 1
    return words_count_dict

words_count_dict = get_count(words)

# Get probability of each word
def get_probs(words_count_dict):
    probs = {}
    m = len(words)
    for i in words_count_dict.keys():
        probs[i]= (words_count_dict.get(i)/m)
    return probs

probs = get_probs(words_count_dict)

# Split word into all possible combinations
word = 'cans'
split_l = [(word[:i],word[i:]) for i in range(len(word)+1)]
delete_l = [(L + R[1:]) for L,R in split_l if len(R)>0]
word[1] + word[1-1] + word[1:]
