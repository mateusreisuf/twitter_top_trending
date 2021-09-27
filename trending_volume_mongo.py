# -*- coding: utf-8 -*-

# Author: Mateus Reis


'''
# Este script tem a função de acessar o banco de dados MongoDB e salvar os
dados em um arquivo com no data.pkl
'''


from pymongo import MongoClient
import pandas as pd


# Conexão com Banco de dados MongoDB
cluster = MongoClient('mongodb+srv://mat:1523a5b6M@cluster0.ihbkd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = cluster['twitter']
collection = db['twitter2']


# busca todos registros no banco de dados
result = collection.find({})


data = []


# salva os registros em uma lista
for x in result:
    data.append(x)


# converte a lista em um DataFrame
data = pd.DataFrame(data)
print(data)


# Salva o DataFrame em um aquivo
data.to_pickle("data.pkl")
