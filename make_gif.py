# -*- coding: utf-8 -*-

# Author: Mateus Reis

'''
Este script gera um gif a partir das imagens presentes na pasta graficos
'''


import imageio
from glob import glob


images = glob('graficos/*.jpg')


gif = []
for i in range(len(images)):
    gif.append(imageio.imread('graficos/'+str(i)+'.jpg'))


imageio.mimsave('movie.gif', gif)