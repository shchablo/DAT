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

def plotParasit(histogram, tokens=[], name='deeply'):

    host = host_subplot(111, axes_class=AA.Axes)
    plt.subplots_adjust(left=0.75)
    par2 = host.twiny()
    par2.axis["left"] = par2.get_grid_helper().new_fixed_axis(loc="left", axes=par2, offset=(-50, 0, 0, 0) )
    par2.axis["left"].toggle(all=True)
    x = np.random.normal(10, 10, 1000)
    y = np.random.normal(10, 10, 1000)
    histogram = h2(x, y, "fixed_width", bin_width=[10, 10], name="Fixed-width bins", axis_names=["x", "y"])
    for i in range(100):
        histogram.fill([40, 40])
    histogram.plot(ax=host)
    plt.savefig(path2save+'to.png')

    return True
