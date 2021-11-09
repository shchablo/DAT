import pandas as pd
import itertools
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist

nltk.download('wordnet')
nltk.download('stopwords')


def get_cleaned_corpus(data, text_column='Tweet Text'):

    """
    Функция принимает на вход датафрейм в исходном виде и возвращает очищенный корпус (список текстов).
    В данный момент из текста удаляется все, кроме слов и чисел, для демонстрации работы.
    ! Требуется выработать концепцию - какие символы мы хотим оставлять.
    Например, хэштеги и собаки наверняка нам следует оставлять. А вот эмодзи, которые никогда не трогают,
    когда проводят анализ тональности текста, нам, по идее, не нужны.
    """

    return data.apply(lambda row: re.sub('\W+', ' ', row[text_column]), axis=1)


def tokenize(corpus, lemmatize=True, del_stopwords=True):

    """
    Функция принимает на вход корпус(список текстов) и возвращает токенизированный корпус (список списков токенов)
    - каждый текст разбит на слова.
    По умолчанию включены удаление частых слов и лемматизация.
    """

    texts = []
    if lemmatize:
        lemm = WordNetLemmatizer()
    if del_stopwords:
        stopwords = nltk.corpus.stopwords.words('english')
    for text in corpus:
        text = str(text).lower().split()
        if lemmatize:
            text = [lemm.lemmatize(word, pos='v') for word in text]  # verbs
            text = [lemm.lemmatize(word, pos='n') for word in text]  # nouns
            # если нужно склеить обратно в текст
            # text = ' '.join(text)
        if del_stopwords:
            text = [word for word in text if word not in stopwords]
        texts.append(text)

    return texts


def clouder(texts, numMostCommonTokens=50):

    """
    This function is given as input texts (the result of tokenizer).
    The result of this function is a dictionary:
        [keys] are the most common tokens (sortet from the most common to least);
        [values] are lists of all tokens from tweets where at least one token is the key.

    INPUTs
        list of list: texts[tweet][tokens];
        numMostCommonTokens - number of most common tokens that will study;
    OUTPUTs
        dictionary: result[key_token][tokens]
    """

    tokens = list(itertools.chain.from_iterable(texts))
    most = FreqDist(tokens).most_common(numMostCommonTokens)
    most = pd.Series(dict(most))
    most = dict(sorted(most.items(), key=lambda item: item[1], reverse=True))
    result = {}
    for token in most.items():
        result[token[0]] = []
        for text in texts:
            if token[0] in text:
                result[token[0]].extend(text)

    return result


def deeper(texts, numMostCommonTokens=50):

    """
    This function is given as input texts (the result of tokenizer).
    The result of this function is a dictionary:
        [keys] are the most common tokens (sortet from the most common to least);
        [values] are lists of all tokens from tweets where at least one token is the key.

    INPUTs
        list of list: texts[tweet][tokens];
        numMostCommonTokens - number of most common tokens that will study;
    OUTPUTs
        dictionary: result[key_token][hist]

        ! Нужно обработать, если в твите больше двух раз встречается слово
    """

    tokens = list(itertools.chain.from_iterable(texts))
    most = FreqDist(tokens).most_common(numMostCommonTokens)
    most = pd.Series(dict(most))
    most = sorted(most.items(), key=lambda item: item[1], reverse=True)
    keys = [value[0] for value in most]
    for token in keys:
        for text in texts:
            if token[0] in text:
                index = text.index(token[0])
                for t in text:
                    if t in keys:
                        print(index, keys.index(t))
                    #h.fiil(token[0], i-index)
    return True
