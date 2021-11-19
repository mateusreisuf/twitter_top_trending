# -*- coding: utf-8 -*-

# Author: Mateus Reis


'''
# Este script tem a função de acessar o banco de dados MongoDB e salvar os
dados em um arquivo com nome data.pkl
'''


from pymongo import MongoClient
import pandas as pd


# Conexão com Banco de dados MongoDB
cluster = MongoClient('')
db = cluster['']
collection = db['']


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
data.to_pickle("volume_data.pkl")
