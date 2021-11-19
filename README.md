# twitter_top_trending

<p align="center"> Este projeto tem como objetivo coletar e analisar o top trending do twitter e fazer análise de sentimento em tweets relacionados aos top trending. </p>



![](https://github.com/mateusreisuf/twitter_top_trending/blob/0023a3333a60b4eb465dcecd577a27e083f70e90/movie.gif)

<h3> Requerimentos: </h3>

<p>python = 3.8</p>

<p>tweepy</p>

<p>pymongo</p>

<p>pandas</p>

<p>matplotlib</p>

<p>numpy</p>

<p>nltk</p>

<h3> Como usar: </h3>

<p>Para coletar os top trending e gerar um gif como da figura acima é preciso seguir esses passos:<p>

<p>executar o comando abaixo para coletar os top trending: <p>

<h5>python top_trending.py</h5>

<p>depois interromper a execução quando achar que possui dados suficientes.<p>

<p>executar o comando abaixo para salvar os dados do mongo em um arquivo:<p>

<h5>python trending_volume_mongo.py</h5>

<p>executar o seguinte comando para gerar os gráficos:<p>

<h5>python graficos.py</h5>

<p>e por fim executar o comando abaixo para gerar um gif:<p>

<h5>python make_gif.py</h5>

<p>Para fazer analise de sentimentos é preciso seguir os seguintes passos:<p>

<p>executar o comando:<p>

<h5>python top_trending_tweets.py </h5>

<p>para coletar tweets relacionados aos top trendings e salvar no mongoDB.<p>

<p>Executar  o comando abaixo para salvar os dados do mongo em um arquivo:<p>

<h5>python tweets_mongo.py</h5>

<p>e por fim executar o comnado abaixo para fazer a filtragem nos tweets e  analise de sentimento:<p>


<h5>python sentiment_analysis.py</h5>

<p>O resultado da analise de sentimentos é um novo dataframe com os tweets originais, os tweets filtrados, a saida do classificador vader e a classificação do sentimento que pode ser positive, neutral ou negative. Por fim para facilitar a analise dos resultados foi criado um jupyter notebook para executar utilize o comando:<p>

<h5>jupyter notebook sentiment_pandas.ipynb</h5>









