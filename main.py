import sys
sys.path.append("units")
sys.path.append("config")

import pandas as pd

from dumper import dump

from tokenizer import get_cleaned_corpus
from tokenizer import tokenize
from tokenizer import clouder
from tokenizer import deeper

from analyzer import freqСloud
from analyzer import plotСloud

from tokenizer import get_cleaned_corpus
from tokenizer import tokenize
from tokenizer import clouder

# ==============================================================================


def unitDumper(path2data, numTweets, behindDays):
    dump(path2data, numTweets, behindDays)
    return True


def unitAnalyzer(path2data, path2save):
    # Let's do simple worldcloud
    freqСloud(path2data, path2save)
    return True

def unitTokenizer(path2data, path2save):

    df = pd.read_csv(path2data, index_col=0)
    data = get_cleaned_corpus(df)
    texts = tokenize(data, lemmatize=True, del_stopwords=True)
    # clouder
    #clouds = clouder(texts, 50)
    #print(clouds.keys())
    #for key in clouds:
    #    plotСloud(' '.join(clouds[key]), path2save, name=key)

    #deeper
    deeps = deeper(texts, 50)

    return True

# ==============================================================================
# ==============================================================================

def main():

    # Use Hydrogen to run this shitte code.
    print("DAT / Deep Anal of Tweets")

    path2data = "./csv/data.csv"
    path2save = "./tests/"
    # Run If you want to get fresh tweets
    #unitDumper(path2data, 2500, 1)

    # Next, add your units for analysis of text data and success with it,
    # or get an anal feeling with your results and do not cry!

    # Let's do simple worldcloud
    #unitAnalyzer(path2data, path2save)

    # Run example for tokenize
    unitTokenizer(path2data, path2save)

    print("The End!")

if __name__ == "__main__":
    main()
