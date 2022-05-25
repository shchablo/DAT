import sys
sys.path.append("units")
sys.path.append("config")

import nltk
nltk.download('omw-1.4')

from dumper import dump
from analyzer import freqСloud

import pandas as pd
from tokenizer import tokenize
from tokenizer import get_cleaned_corpus

from sklearn.feature_extraction.text import CountVectorizer
from yellowbrick.text import FreqDistVisualizer
from yellowbrick.datasets import load_hobbies

from collections import Counter

def hydrogen():

    # Use Hydrogen to run this shitte code.
    print("DAT / Deep Anal of Tweets")

    path2data = "./csv/data.csv"; path2save = "./tests/"

    # Run If you want to get fresh tweets
    dump(path2data, 35, 1)

    # Next, add your units for analysis of text data and success with it,
    # or get an anal feeling with your results and do not cry!

    # Let's do simple worldcloud

    #freqСloud(path2data, path2save)
    corpus = get_cleaned_corpus(pd.read_csv(path2data), text_column='Tweet Text')
    tokens = tokenize(corpus, lemmatize=True, del_stopwords=True)
    flat_list = [item for sublist in tokens for item in sublist]
    counts = Counter(flat_list)
    print(counts)

def main():
    print("I'm empty")
    hydrogen()

if __name__ == "__main__":
    main()
