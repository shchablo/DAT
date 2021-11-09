import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def freqСloud(path2data, path2save, name='WordCloud', text_column='Tweet Text'):

    file = path2save + name + ".png"
    df = pd.read_csv(path2data, index_col=0)
    text = ''
    for index, row in df.iterrows():
        text += row[text_column]
    wordcloud = WordCloud(width=3800, height=1600).generate(text)
    plt.figure(figsize=(20, 10), facecolor='k')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(file)

    return True


def plotСloud(data, path2save, name='cloud'):

    file = path2save + name + ".png"
    wordcloud = WordCloud(width=3800, height=1600).generate(data)
    plt.figure(figsize=(20, 10), facecolor='k')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(file)

    return True
