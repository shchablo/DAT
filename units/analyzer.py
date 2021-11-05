# Start with loading all necessary libraries
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

def freqСloud(path2data, path2save):
    file = path2save + "WordCloud.png"
    df = pd.read_csv(path2data, index_col=0)
    df.head()
    text = ''
    for index, row in df.iterrows():
        text += row['Tweet Text']

        wordcloud = WordCloud(width=3800, height=1600).generate(text)
        plt.figure( figsize=(20,10), facecolor='k')
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.savefig(file)
        plt.show()
