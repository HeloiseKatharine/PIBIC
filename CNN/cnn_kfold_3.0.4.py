from os import P_NOWAIT
from numpy.core.defchararray import array, index
from sklearn.utils.validation import check_random_state
import tensorflow as tf 
from tensorflow import keras
import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt
import datetime
from sklearn.model_selection import KFold, StratifiedKFold 
import pandas as pd
from tensorflow.python.autograph.operators.py_builtins import print_
from tensorflow.python.keras.backend import backend, clear_session

IMAGE_SIZE = [224, 224]#tamanho da entrada 

#localização das pastas do teste e do treino
train = '/content/drive/MyDrive/Colab Notebooks/train'

data_train = [] 
data_test = []

import os

#teste 
treino_M_treino_B = '/content/drive/MyDrive/Colab Notebooks/train'

#treinamento
#treino_M = '/content/drive/MyDrive/Colab Notebooks/train/M'
#treino_B = '/content/drive/MyDrive/Colab Notebooks/train/B'

treino_M = 'D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train\\M'
treino_B = 'D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train\\B'

#treino_M = ['/content/drive/MyDrive/Colab Notebooks/train/M/{}'.format(i) for i in os.listdir(treino_M)]
#treino_B = ['/content/drive/MyDrive/Colab Notebooks/train/B/{}'.format(i) for i in os.listdir(treino_B)]

treino_M = ['D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train\\M\\{}'.format(i) for i in os.listdir(treino_M)]
treino_B = ['D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train\\B\\{}'.format(i) for i in os.listdir(treino_B)]

#validação/teste
'''
teste_M = '/content/drive/MyDrive/Colab Notebooks/train/M'
teste_B = '/content/drive/MyDrive/Colab Notebooks/train/B'

teste_M = ['/content/drive/MyDrive/Colab Notebooks/train/M/{}'.format(i) for i in os.listdir(teste_M)]
teste_B = ['/content/drive/MyDrive/Colab Notebooks/train/B/{}'.format(i) for i in os.listdir(teste_B)]
'''

data_labels = []

for i in treino_B:
  data_labels.append(0)# benigno = 0 maligno = 1

for i in treino_M:
  data_labels.append(1)# benigno = 0 maligno = 1

data_train = treino_B + treino_M #benigno e maligno 

data_train_labels = [] #criando uma lista de imagens e labels

#tranformei todos os dados da lista data_train em uma lista (lista aninhada)
for i in data_train:
  data_train_labels.append([i])

#adicionado o label em cada lista 
for i in range (0, len(data_train_labels)):
    data_train_labels[i].append(data_labels[i])

#dataframe

import pandas as pd

colunas = ['train', 'labels'] #criando as colunas

df = pd.DataFrame(data=data_train_labels, columns = colunas)

#VGG16 | MODEL

#Instanciando o modelo VGG16
from tensorflow import keras

vgg = keras.applications.vgg16.VGG16(
  input_shape = IMAGE_SIZE + [3],
  weights = 'imagenet', #pesos pré-treinados do imagenet (transfer-learning workflow)
  include_top = False
)

#vgg.input
vgg.output

#"congelar" o modelo básico
for layer in vgg.layers:
  layer.trainable = False

x = keras.layers.Flatten()(vgg.output)
prediction = keras.layers.Dense(2, activation='softmax')(x) #duas classes (B e M)
model = keras.Model(inputs=vgg.input, outputs=prediction)
    
model.summary()

adam = keras.optimizers.Adam()

train_datagen = keras.preprocessing.image.ImageDataGenerator(
    preprocessing_function=keras.applications.vgg16.preprocess_input,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

test_datagen = keras.preprocessing.image.ImageDataGenerator(
    preprocessing_function= keras.applications.vgg16.preprocess_input,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

#KFOLD

Y = df.labels

kf = KFold(n_splits = 3)#5
                         
skf = StratifiedKFold( 3, random_state = 7, shuffle = True)#5

def get_model_name(k):
    return 'model_'+str(k)+'.h5'



VALIDATION_ACCURACY = []
VALIDAITON_LOSS = []
save_dir = '/saved_models/'

fold_var = 1


for train_index, val_index in kf.split(df,Y):

  training_data = df.iloc[train_index]
  validation_data = df.iloc[val_index]

  treinamento_data = train_datagen.flow_from_dataframe(
    training_data,
    directory= 'D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\image_dir',
    #directory = "/content/drive/MyDrive/Colab Notebooks/image_dir",
    x_col="train",
    y_col="labels",
    target_size = (224, 224),
    #batch_size = 2, 
    #class_mode = "categorical",
    shuffle = True,
    class_mode=None
    )
  
  validacao_data = train_datagen.flow_from_dataframe(
    validation_data,
    directory= 'D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\image_dir',
    #directory = "/content/drive/MyDrive/Colab Notebooks/image_dir",
    x_col="train",
    y_col="labels",
    target_size = (224, 224),
    #batch_size = 2, 
    #class_mode = "categorical",
    shuffle = True,
    class_mode=None
    )
  
  #compilando o model
  model.compile(
    loss='binary_crossentropy',#loss
    optimizer=adam,
    metrics=['accuracy'])
  
  
  checkpoint = keras.callbacks.ModelCheckpoint(
    save_dir+get_model_name(fold_var),
    monitor='val_accuracy',
    #filepath='mymodel.h5',
    verbose=2,#?
    save_best_only=True,
    mode='max')

  lista_callbacks = [checkpoint]

  # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO da Parte de Treinamento >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
  print(type(treinamento_data))


  model_history = model.fit(
    treinamento_data,
    validation_data=validacao_data,
    epochs=30
    )

  #steps_per_epoch=5,
  #callbacks= lista_callbacks,
  #epochs=10,
  #callbacks = lista_callbacks)
  

  fold_var += 1
  # https://datascience.stackexchange.com/questions/85447/valueerror-no-gradients-provided-for-any-variable