# https://machinelearningmastery.com/k-fold-cross-validation/
# https://machinelearningmastery.com/how-to-configure-k-fold-cross-validation/

# https://scikit-learn.org/stable/modules/cross_validation.html
# https://medium.com/data-hackers/como-criar-k-fold-cross-validation-na-m%C3%A3o-em-python-c0bb06074b6b



from numpy.lib.function_base import append
from sklearn.model_selection import KFold, StratifiedKFold 

import os

treino_M = 'D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train\\M'
treino_B = 'D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train\\B'
treino_M = ['D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train\\M\\{}'.format(i) for i in os.listdir(treino_M)]
treino_B = ['D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train\\B\\{}'.format(i) for i in os.listdir(treino_B)]

data_train_labels = []

data_train = treino_B + treino_M #benigno e maligno 

kfold = KFold(3, True, 1) 

import pandas as pd
import numpy 

a = numpy.array(data_train)
#print(a)


# enumerate splits
#for train, test in kfold.split(a):
	#print('train: %s, test: %s' %(train, test))
    #print('train: %s, test: %s' % (a[train], a[test]))

lista1 = [1,2,3,4,5]
lista2 = ['afd','b','c','d','e']
lista = []

print("teste")
 

#*****************DEU CERTO*********************
lista_aux = []

#tranformei todos os dados da lista em uma lista 
for i in range (0, len(lista2)):
    print(i)
    lista_aux.append(list(lista2[i][::]))

print('lista_aux')
print(lista_aux) 

#adicionado um valor em cada lista 
for i in range (0, len(lista2)):
    lista_aux[i].append(lista1[i])

print('lista_aux_2')
print(lista_aux) 


#*****************DEU CERTO*********************


lista2.append(list(lista2[0]))

print(lista2)
#lista2[5][1].append(str(lista1[0]))
lista2[5].append('ola')

print(lista2)


#**************************************



for i in range(0, len(lista1)):
    print(lista1[i])
    #lista1[i].append(lista2[i])
    #lista[i].append( lista1[i])
    #lista[i].append( lista2[i])

print(lista)
print("Resposta:\n")
print(lista1)
