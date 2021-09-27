# twitter_top_trending

<p align="center"> Este projeto tem como objetivo coletar e analisar o top trending do twitter e fazer análise de sentimento em tweets relacionados aos top trending. </p>



![](https://github.com/mateusreisuf/twitter_top_trending/blob/0023a3333a60b4eb465dcecd577a27e083f70e90/movie.gif)

<h3> Requerimentos: <h3>

python = 3.8

tweepy

googletrans==4.0.0rc1

pymongo

pandas

numpy

nltk

<h3> Como usar: <h3>

Para coletar os top trending e gerar um gif como da figura acima é preciso seguir esses passos:

executar o comando abaixo para coletar os top trending: 

python top_trending.py

depois interromper a execução quando achar que possui dados suficientes.

executar o comando abaixo para salvar os dados do mongo em um arquivo:

python trending_volume_mongo.py

executar o seguinte comando para gerar os gráficos:

python graficos.py

e por fim executar o comando abaixo para gerar um gif:

python make_gif.py



Para fazer analise de sentimentos é preciso seguir os seguintes passos:

executar o comando:

python top_trending_tweets.py 

para coletar tweets relacionados aos top trendings e salvar no mongoDB.

Executar  o comando abaixo para salvar os dados do mongo em um arquivo:

python tweets_mongo.py

e por fim executar o comnado abaixo para fazer analise de sentimento nos tweets:

python sentiment_analysis.py

O resultado da analise de sentimentos é um dicionário que contem os nomes dos top trending

e uma classificação em relação ao sentimento que pode assumir 3 valores neutral , positive ou negative.







