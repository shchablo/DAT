import pandas as pd
import re
import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('stopwords')

path2data = "./csv/data.csv";

def get_cleaned_corpus(df, text_column='Tweet Text'):
    """
    Функция принимает на вход датафрейм в исходном виде и возвращает очищенный корпус(список текстов).
    В данный момент из текста удаляется все, кроме слов и чисел, для демонстрации работы.
    ! Требуется выработать концепцию - какие символы мы хотим оставлять.
    Например, хэштеги и собаки наверняка нам следует оставлять. А вот эмодзи, которые никогда не трогают,
    когда проводят анализ тональности текста, нам, по идее, не нужны
    """
    return df.apply(lambda row: re.sub('\W+', ' ', row[text_column]), axis = 1)

def tokenize(corpus, lemmatize=True, del_stopwords=True):
    """
    Функция принимает на вход корпус(список текстов) и возвращает токенизированный корпус(список списков токенов)
    - каждый текст разбит на слова.
    По умолчанию включены удаление частых слов и лемматизация.
    """
    texts = []
    if lemmatize == True:
        lemm = WordNetLemmatizer()
    if del_stopwords == True:
        stopwords = nltk.corpus.stopwords.words('english')
    for text in corpus:
        text = str(text).lower().split()
        if lemmatize == True:
            text = [lemm.lemmatize(word, pos = 'v') for word in text] # for verbs
            text = [lemm.lemmatize(word, pos = 'n') for word in text] # for nouns

            #если нужно склеить обратно в текст
            #text = ' '.join(text)
        if del_stopwords == True:
            text = [word for word in text if word not in stopwords]
        texts.append(text)

    return texts
