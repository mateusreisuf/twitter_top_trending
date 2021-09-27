# -*- coding: utf-8 -*-

# Author: Mateus Reis

'''
# Este script tem a função de acessar a API do Twitter para coletar o top trending
a cada minuto e armazenar no banco de dados MongoDB
'''


import tweepy
import json
from datetime import datetime
import time
from pymongo import MongoClient



# Conexão com Banco de dados MongoDB
cluster = MongoClient('mongodb+srv://mat:1523a5b6M@cluster0.ihbkd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['twitter']
collection = db['twitter3']


# Autenticações com API do Twitter
consumer_key = '5mQcLHMi40bohlYDR5BaINf5E'
consumer_secret = 'i3EuLk0R5YsWXsStm0VmXBXcFtRACw4j86QeJlS44XhPYQlsnS'
access_token = '1441027346946011136-UFreliJiI39fxhNiVOBxDQViPpsp28'
access_token_secret = '3dMsYyMTi46yd4l0uvhYN7imAx4scevI3q08vwSL1qMgq'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


BRAZIL_WOE_ID = 23424768
id = 0


def trending(id):
    # obtem a data e hora do computador
    now = datetime.now()

    # formata data e hora nesse formato : dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    # separa a data da hora
    dt_string = dt_string.split(sep=' ')

    brazil_trends = api.trends_place(BRAZIL_WOE_ID)

    trends = json.loads(json.dumps(brazil_trends, indent=1))

    trends2 = []
    for trend in trends[0]['trends']:
        if trend['tweet_volume'] is not None and trend['tweet_volume'] > 10000:
            #print(trend)
            trends2.append((trend['name'], trend['tweet_volume'],dt_string))


    # ordena a lista de top trendings pelo volume
    trends2.sort(key=lambda x:-x[1])

    aux = []
    for x in trends2:
        x = {'_id':id,'name':x[0],'date':dt_string[0],'hour':dt_string[1],'volume':x[1]}

        # condição para evitar inserção redundante
        if(x['name'] not in aux):
            collection.insert_one(x)
            id += 1
            print(x)


        aux.append(x['name'])

    # delay para evitar que seja a feita uma leitura redundante
    time.sleep(1)
    return id



while(True):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    dt_string = dt_string.split(sep=' ')
    date = dt_string[0]
    hour = dt_string[1]
    hour2, minutes, seconds = hour.split(sep=':')

    # Caso queira mostrar a hora no terminal descomente a linha abaixo:
    #print(hour2, minutes, seconds, sep =':')


    # sempre que os segundos estiverem em '00' coleta o top trending
    if (seconds == '00'):
        id = trending(id)
    time.sleep(0.5)
