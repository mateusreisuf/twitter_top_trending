# -*- coding: utf-8 -*-

# Author: Mateus Reis


'''
Este script faz filtragem dos tweets e analise de sentimento em tweets presentes no aquivo sentiment_data.pkl 
e salva no arquivo sentiment_data_results.pkl
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time
import re
import string


data = pd.read_pickle("sentiment_data.pkl")
data = data.drop(columns=['_id'])

print(data.head())


unique_names = data["name"].unique()


# Instancia o classificador de sentimento
sid = SentimentIntensityAnalyzer()

average_sentiment = []
sentiments = []
translated = []
filtered = []


def split(word):
    return [char for char in word]


def remove_emojis(data):
    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  
        u"\U0001F300-\U0001F5FF"  
        u"\U0001F680-\U0001F6FF"  
        u"\U0001F1E0-\U0001F1FF"  
        u"\U00002500-\U00002BEF"  
        u"\U00002702-\U000027B0"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                      "]+", re.UNICODE)
    return re.sub(emoj, '', data)


# Função utilizada para filtrar os tweets
def filter(text):

    remove = [',','.','RT','/','*','[',']','\\',"'",'"']


    for x in remove:
        text = text.replace(x,'')

    text = text.split()

    text = [x for x in text if not '#' in x and not '@' in x]

    text = " ".join(text)

    text = remove_emojis(text)

    text = re.sub(r"http\S+", "", text)

    letters = string.ascii_letters
    digits = string.digits

    letters = split(letters)

    digits = [str(x) for x in digits]

    characters = letters + digits

    characters.append(' ')



    for c in text:
        if c not in characters:

            text.replace(c,'')
    print(text)
    return text

scores = []

for i in range(len(unique_names)):
    data_name = data.loc[data['name'] == unique_names[i]]
    name = unique_names[i]
    print(name)
    data_name = data_name.drop(columns=['name'])
    data_name = data_name.values
    aux = []

    neg = 0
    neu = 0
    pos = 0
    c = 0
    # traduz o tweet para ingles e calcula a saida do classificador de sentimento e faz a média
    for element in data_name:
        element = str(element)
        element = filter(element)
        filtered.append(element)

        element = sid.polarity_scores(element)
        prediction = element['compound']
        scores.append(prediction)
        aux.append(prediction)

        if (prediction < -0.15):
            sentiment = 'negative'
            neg+=1
        elif (prediction > -0.15) and (prediction < 0.15):
            sentiment = 'neutral'
            neu+=1
        elif (prediction > 0.15):
            sentiment = 'positive'
            pos+=1
        sentiments.append(sentiment)

        if(c % 50 == 0):
            print(f'Nome : {name},  Processado  {(c/len(data_name))*100 :.2f} % ')
        c += 1



    average = np.mean(aux)
    neg_score = neg/len(aux)
    neu_score = neu/len(aux)
    pos_score = pos/len(aux)
    print(name,'neg: ',neg_score,'neu: ',neu_score,'pos: ',pos_score,'compound: ',average)

    if(average < -0.15):
        average = 'negative'
    elif(average > -0.15)and(average < 0.15):
        average = 'neutral'
    elif(average > 0.15):
        average = 'positive'
    average_sentiment.append(average)
    

zip_iterator = zip(unique_names,average_sentiment)
result = dict(zip_iterator)

print(result)


result = np.array(result)


print(len(sentiments))

data['filtered'] = filtered

data['sentiment'] = sentiments

data['score'] = scores

# Salva o novo dataframe
data.to_pickle("sentiment_data_results.pkl")
