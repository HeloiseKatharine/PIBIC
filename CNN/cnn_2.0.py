import tensorflow as tf 
from tensorflow import keras
Epocas               = 50
#from keras import layers
#from keras import models

import numpy as np 
import os
import random
import cv2 as cv
import matplotlib.pyplot as plt

#localizando as pastas e pegando todas as imagens de cada uma delas

#ainda tem que fazer com a pasta de testes
teste = 'C:\\Users\\heloh\\Desktop\\testeCNN\\train\\teste' #não está usando

treino_M = 'C:\\Users\\heloh\\Desktop\\testeCNN\\train\\M' #maligno
treino_B = 'C:\\Users\\heloh\\Desktop\\testeCNN\\train\\B' #benigno
treino_N =  'C:\\Users\\heloh\\Desktop\\testeCNN\\train\\Normal' #benigno

#pegando todas as fotos 
treino_M = ['C:\\Users\\heloh\\Desktop\\testeCNN\\train\\M\\{}'.format(i) for i in os.listdir(treino_M)]  #maligno
treino_B = ['C:\\Users\\heloh\\Desktop\\testeCNN\\train\\B\\{}'.format(i) for i in os.listdir(treino_B)]  #benigno

treino_N = ['C:\\Users\\heloh\\Desktop\\testeCNN\\train\\Normal\\{}'.format(i) for i in os.listdir(treino_N)]  #normal

teste_imagens = ['C:\\Users\\heloh\\Desktop\\testeCNN\\train\\teste\\{}'.format(i) for i in os.listdir(teste)] #teste


#redimencionando as imagens 100 x 100

linhas = 150 #quantidade de linhas
colunas = 150 #quantidade de colunas
channels = 1  #1 = tons cinza

tam_m = len(treino_M)
tam_b = len(treino_B)
treino_BM = treino_M + treino_B
tam_bm = len(treino_BM)

#retorna uma lista com as imagens redimencionadas e uma lista com as labels

def redimensionar_imagens(lista_imagens, m, b, bm):

    imagens = []
    labels = [] 
    
    for i in range(0,m):
       
        imagens.append(cv.resize( cv.imread(lista_imagens[i]), (linhas,colunas), interpolation=cv.INTER_CUBIC))

        labels.append(0)# benigno = 1 maligno = 0

    for j in range(b,bm):
        imagens.append(cv.resize( cv.imread(lista_imagens[j]), (linhas,colunas), interpolation=cv.INTER_CUBIC))

        labels.append(1)# benigno = 1 maligno = 0
      
    return imagens, labels


treino_imagens, treino_labels = redimensionar_imagens(treino_BM, tam_m , tam_b, tam_bm)#armazena os dados em duas listas 


#transformando em arrys
treino_imagens = np.array(treino_imagens)
treino_labels = np.array(treino_labels)

'''
imagens_train, imagens_val, labels_train, labels_val =  sklearn.model_selection.train_test_split(treino_imagens, treino_labels, test_size=0.20, random_state=2)
'''


#------------------------------Construindo o modelo------------------------------

#modelo 
model = keras.Sequential()
model.add(keras.Input(shape=(150, 150, 3)))  # 250x250 RGB images
model.add(keras.layers.Conv2D(32, 5, strides=2, activation="relu"))
model.add(keras.layers.Conv2D(32, 3, activation="relu"))
model.add(keras.layers.MaxPooling2D(3))

'''
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(5,linhas, colunas, channels)),
    keras.layers.Dense(128, activation='relu'), #possui 128 nós 
    keras.layers.Dense(10, activation='softmax') #Um array de 10 probabilidades que são somadas e retorna 1 probabilidade.
])
'''

#*************************************************************************************************************************

model = tf.keras.models.Sequential()

model.add(tf.keras.layers.Conv2D(32, (1, 1), activation='relu',input_shape=(150, 150, 1)))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))

model.add(tf.keras.layers.Conv2D(64, (1, 1), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))

model.add(tf.keras.layers.Conv2D(128, (1, 1), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))

model.add(tf.keras.layers.Conv2D(128, (1, 1), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))

model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dropout(0.5))  #Dropout for regularization
model.add(tf.keras.layers.Dense(512, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))  #Sigmoid function at the end because we have 

#compilando o modelo
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics = ['accuracy']) 

#treinando o modelo 
model.fit(treino_imagens, treino_labels, epochs=10) 

