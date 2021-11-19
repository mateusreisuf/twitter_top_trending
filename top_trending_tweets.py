# -*- coding: utf-8 -*-

# Author: Mateus Reis


'''
Este script verifica quais são os top trending e depois fica buscando tweets relacionados
e salva no banco de dados mongoDB
'''


import numpy as np
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Stream
import tweepy
import json
from pymongo import  MongoClient


# Conexão com Banco de dados MongoDB
cluster = MongoClient('')
db = cluster['']
collection = db['']


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if not status.truncated:
            text = status.text
        else:
            text = status.extended_tweet['full_text']


        # busca se o nome do top tranding esta presente no tweet e salva no banco de dados
        for word in keywords_to_track:
            if word in text:
                data = {'name':word,'text':text}
                collection.insert_one(data)
                #print(word,' - ',text)
                pos = keywords_to_track.index(word)
                lista[pos]+=1


        # Lista com a quantidade de tweets por top tranding
        print(lista)
        print('\n')


# Autenticações com API do Twitter
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)


EUA_WOE_ID = 23424977

EUA_trends = api.trends_place(EUA_WOE_ID)

trends = json.loads(json.dumps(EUA_trends, indent=1))

trends2 = []

for trend in trends[0]['trends']:

    if trend['tweet_volume'] is not None and trend['tweet_volume'] > 10000:
        trends2.append([trend['name'],trend['tweet_volume']])


# Ordena em relação ao volume de forma decrescente
trends2.sort(key=lambda x:-x[1])
trends2 = [x[0] for x in trends2]


# Seleciona os 10 com maior volume
keywords_to_track = trends2[:10]




print(keywords_to_track)
print('--------------------')

lista = np.zeros(10)


# Instancia um objeto SListener
listen = MyStreamListener()


# Instancia um objeto Stream
stream = Stream(auth, listen)


# Começa a coletar dados
stream.filter(track = keywords_to_track,languages=['en'])


