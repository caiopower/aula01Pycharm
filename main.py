# This is a sample Python script.
import time

import numpy
import plotly

#1 Exemplo de criação
#ndarray1 = numpy.zeros(100000)
#print(f' 1- Conteúdo da Lista: {ndarray1}, o tamanho: {len(ndarray1)}')
#ndarray1 = numpy.ones(100000)
#print(f'2- Conteúdo da Lista: {ndarray1}, o tamanho: {len(ndarray1)}')
#ndarray1 = numpy.linspace(10, 1000, 1000)
#print(f' 3- Conteúdo da Lista: {ndarray1}, o tamanho: {len(ndarray1)}')

# 2 - Comparar desempenho
#start_time = time.time()
#lista = [0] * 1000000000
# = time.time()
#elapsed_time = end_time - start_time
#print(f'A criação e lista de 1 bilhão de elementos levou: {elapsed_time}')

#start_time = time.time()
#ndarray = numpy.zeros(1000000000)
#end_time = time.time()
#elapsed_time = end_time - start_time
#print(f'A criação e lista de 1 bilhão de elementos levou: {elapsed_time}')

##3 - Da para fazer ainda melhor se definirmos o tipo de dado, exemplo: dado tipo int8 (para calores de 0 - 255)
#start_time = time.time()
#ndarray_uint8 = numpy.zeros(1000000000, dtype='uint8')
#end_time = time.time()
# = end_time - start_time
#print(f'A criação de um ndarray de 1 bilhao de elementos em int de 8 não sinalizado levou: {elapsed_time}')


