import sys
sys.path.append("units")
sys.path.append("config")

from wordcloud import WordCloud

import pandas as pd
#===
from dumper import dump
#===
from analyzer import freqСloud
#===
from tokenizer import tokenize
from tokenizer import get_cleaned_corpus

def hydrogen():

    # Use Hydrogen to run this shitte code.
    print("DAT / Deep Anal of Tweets")

    path2data = "./csv/data.csv"; path2save = "./tests/"

    # Run If you want to get fresh tweets
    dump(path2data, 3000, 1)

    # Next, add your units for analysis of text data and success with it,
    # or get an anal feeling with your results and do not cry!

    # Let's do simple worldcloud
    freqСloud(path2data, path2save)

    # Run example for tokenize
    df = pd.read_csv(path2data, index_col=0)
    df.head()
    data = get_cleaned_corpus(df)
    texts = tokenize(data, lemmatize=True, del_stopwords=True)
    print(texts)
# Create and generate a word cloud image:
for i in range(len(texts)):
    print(texts[i])
wordcloud = WordCloud().generate(texts)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

def main():
    print("I'm empty")

if __name__ == "__main__":
    main()
