# -*- coding: utf-8 -*-

# Author: Mateus Reis


'''
Este script faz analise de sentimento em tweets presentes no aquivo sentiment_data.pkl
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns
from googletrans import Translator, constants
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Cria um objeto utilizado para fazer a tradução de texto
translator = Translator()


data = pd.read_pickle("sentiment_data.pkl")
data = data.drop(columns=['_id'])

print(data.head())


unique_names = data["name"].unique()


# Instancia o classificador de sentimento
sid = SentimentIntensityAnalyzer()

average_sentiment = []

for i in range(len(unique_names)):
    data_name = data.loc[data['name'] == unique_names[i]]
    name = unique_names[i]
    data_name = data_name.drop(columns=['name'])
    data_name = data_name.values
    aux = []
    neg = []
    neu = []
    pos = []
    # traduz o tweet para ingles e calcula a saida do classificador de sentimento e faz a média
    for element in data_name:
        element = str(element)
        element = translator.translate(element,dest = 'en')
        element = element.text
        element = sid.polarity_scores(element)
        aux.append(element['compound'])
        neg.append(element['neg'])
        neu.append(element['neu'])
        pos.append(element['pos'])


    average = np.mean(aux)
    avg_neg = np.mean(neg)
    avg_neu = np.mean(neu)
    avg_pos = np.mean(pos)
    print(name,'neg: ',avg_neg,'neu: ',avg_neu,'pos: ',avg_pos,'compound: ',average)
    sentiment_list = [avg_neg,avg_neu,avg_pos]
    pos = sentiment_list.index(max(sentiment_list))
    if(pos == 0):
        average = 'negative'
    elif(pos == 1):
        average = 'neutral'
    elif(pos == 2):
        average = 'positive'
    average_sentiment.append(average)
    #print(data_name)

zip_iterator = zip(unique_names,average_sentiment)
result = dict(zip_iterator)

print(result)


result = np.array(result)
np.save('result_sentiment.npy',result)