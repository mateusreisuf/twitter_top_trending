# -*- coding: utf-8 -*-

# Author: Mateus Reis


'''
Este script gera graficos de barras do top trending com os dados contidos no arquivo data.pkl
o volume é calculado no intervalo de 1 minuto
'''


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from googletrans import Translator, constants
from datetime import datetime
from datetime import timedelta


save_dir = 'graficos'
if not os.path.exists(save_dir):
    os.mkdir(save_dir)


# Cria um objeto utilizado para fazer a tradução de texto
translator = Translator()


data = pd.read_pickle("volume_data.pkl")


# Mostra no terminal os 5 primeiros registros no DataFrame
print(data.head())


# Salva as datas distintas em uma lista
unique_dates = data["date"].unique()


img_num = 0


# Base de dados é filtrada pela data
for i in range(len(unique_dates)):
    date = unique_dates[i]
    data_in_date = data.loc[data['date'] == date]
    unique_hours = data_in_date['hour'].unique()
    last = []
    memo = []

    colors = ['y','b','red','green','orange','purple','gray','pink','olive','cyan']
    colors.reverse()
    # Base de dados é filtrada pela hora
    for j in range(len(unique_hours)):

        hour  = unique_hours[j]
        print(date,hour)


        data_in_hour = data_in_date.loc[(data_in_date["hour"] == hour) & (data_in_date['date'] == date)]
        #x,y = teste['name'].values,teste['volume'].values
        data_in_hour = data_in_hour.drop(['_id','date', 'hour'], axis=1)
        data_in_hour = data_in_hour.values


        px = []
        py = []
        aux = []

        # Calcula a diferença entre a leitura atual e a de um minuto atrás dos top trendings e armazena na lista aux
        if(len(last)>0):
            #print(x.shape,last.shape)
            for k in range(data_in_hour.shape[0]):
                #print(x[k])
                element = data_in_hour[k]
                name,volume = element
                if name in last:
                   indice = np.where(last == name)
                   indice = indice[0]
                   element2 = last[indice,:]
                   element2 = element2[0]
                   volume2 = element2[1]
                   dv = volume - volume2

                   # Considera apenas top trendings que tiveram crescimento no ultimo minuto
                   if(dv > 0) and (dv != 0):
                    aux.append([name,dv])


            # Ordenas os top trending pelo volume
            aux.sort(key=lambda x: -x[1])


            # Salva os nomes e volumes em lista separadas para plotagem
            for p in range(len(aux)):
                aux_name,aux_dv = aux[p]
                px.append(aux_name)
                py.append(aux_dv)


            fig, ax = plt.subplots(figsize=(20.8, 11.7))


            # Para facilitar a visualização mostra apenas o top 10
            px = px[:10]
            py = py[:10]

            px.reverse()
            py.reverse()


            # Verifica se o nome do top trending esta na tabela ascii e caso nao esteja traduz para o ingles
            px = [x if x.isascii() else translator.translate(x,dest='en').text for x in px]
            #print(px)
            #print(p_l)
            #print(py)
            #colors = ['c','y','gray','pink','brown','purple','red','green','orange','blue']

            for l in range(len(px)):
                plt.barh(px[l], py[l],color = colors[l])
                #plt.barh(px[l], py[l])


            day, month, year = date.split(sep = '/')

            date_iso = year + '-' + month + '-' + day


            now_datetime = date_iso + ' ' + hour
            now_datetime = datetime.fromisoformat(now_datetime)

            prev_datetime = now_datetime - timedelta(seconds=0, minutes=1, hours=0)
            prev_hour = prev_datetime.strftime("%H:%M:%S")

            # se a data for a mesma de um minuto atrás
            if (now_datetime.day == prev_datetime.day):

                ax.set_title('Twitter Top Trendings' + ' - ' + date + ' - ' + prev_hour + ' - ' +hour,
                         loc='center', )

            else:

                prev_date = prev_datetime.strftime("%d/%m/%Y")
                ax.set_title('Twitter Top Trendings' + ' - ' + prev_date + ' - ' + prev_hour + ' - ' + date + ' - ' + hour,
                             loc='center', )

            ax.xaxis.set_tick_params(pad=5)
            ax.yaxis.set_tick_params(pad=10)
            plt.xlabel(' Variação do Volume')
            plt.savefig('graficos/' + str(img_num) + '.jpg',dpi = 100)

            img_num += 1
            #plt.show()
            plt.close()


        last = data_in_hour



