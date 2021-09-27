# -*- coding: utf-8 -*-

# Author: Mateus Reis

'''
Este script tem a função de acessar o banco de dados MongoDB com os tweets no arquivo
sentiment_data.pkl para posterior analise de sentimentos
'''


import pymongo
from pymongo import  MongoClient
import numpy as np
import pandas as pd


# Conexão com Banco de dados MongoDB
cluster = MongoClient('mongodb+srv://mat:1523a5b6M@cluster0.ihbkd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['twitter']
collection = db['tweets']


result = collection.find({})


data = []
for x in result:
    data.append(x)


data = pd.DataFrame(data)
print(data)


data.to_pickle("sentiment_data.pkl")