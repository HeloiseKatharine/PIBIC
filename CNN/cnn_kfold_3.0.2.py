# fontes:
# https://github.com/jeffheaton/t81_558_deep_learning/blob/master/t81_558_class_05_2_kfold.ipynb
# https://medium.com/the-owl/k-fold-cross-validation-in-keras-3ec4a3a00538
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html
# https://www.dobitaobyte.com.br/como-criar-um-dataset-para-deep-learning/
# https://www.pyimagesearch.com/2018/05/07/multi-label-classification-with-keras/ 
# https://vijayabhaskar96.medium.com/multi-label-image-classification-tutorial-with-keras-imagedatagenerator-cd541f8eaf24
# https://keras.io/api/applications/vgg/#vgg16-function
# https://keras.io/guides/transfer_learning/
# https://algoritmosempython.com.br/cursos/programacao-python/listas/
# https://machinelearningmastery.com/k-fold-cross-validation/
# https://machinelearningmastery.com/how-to-configure-k-fold-cross-validation/
# https://www.youtube.com/watch?v=LxvFuLDXUdk

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

#from tensorflow import backend, clear_session
#from keras import backend , clear_session

IMAGE_SIZE = [224, 224]#tamanho da entrada 

#localização das pastas do teste e do treino
train = 'D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train'
test = 'D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\test'

#**********************************************
data_train = [] 
data_test = []

import os

treino_M = 'D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train\\M'
treino_B = 'D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train\\B'

treino_M = ['D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train\\M\\{}'.format(i) for i in os.listdir(treino_M)]
treino_B = ['D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train\\B\\{}'.format(i) for i in os.listdir(treino_B)]


#print('********TESTE**********')

data_labels = []

for i in treino_B:
  data_labels.append(0)# benigno = 0 maligno = 1

for i in treino_M:
  data_labels.append(1)# benigno = 0 maligno = 1


#**********************************************




data_train = treino_B + treino_M #benigno e maligno 



#**********************************************
#print('********TESTE**********')


data_train_labels = [] #criando uma lista de imagens e labels

#tranformei todos os dados da lista data_train em uma lista (lista aninhada)
for i in data_train:
  data_train_labels.append([i])

#print('data_train_labels')
#print(data_train_labels)

#adicionado o label em cada lista 
for i in range (0, len(data_train_labels)):
    data_train_labels[i].append(data_labels[i])

#print('data_train_labels ungndvhdfhggbuf')
#print(data_train_labels)

#print('********TESTE**********')





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO da validação cruzada >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#**********************************************

Y = data_labels

kf = KFold(3, random_state = 7, shuffle = True)

#comentar
idg = keras.preprocessing.image.ImageDataGenerator( preprocessing_function=keras.applications.vgg16.preprocess_input,
                                                    rotation_range=40,
                                                    width_shift_range=0.2,
                                                    height_shift_range=0.2,
                                                    shear_range=0.2,
                                                    zoom_range=0.2,
                                                    horizontal_flip=True,
                                                    fill_mode='nearest') 


def get_model_name(k):
  return 'model_'+str(k)+'.h5'

save_dir = '/saved_models/'
fold_var = 1


#**********************KFOLD************************

data_train_labels = array(data_train_labels)#transforma em array


VALI_ACURACIA = []
VALI_LOSS = []
image_dir = '/image_dir/' 



#for train_index, val_index in kf.split(data_train_labels, Y):
for train_index, val_index in kf.split(data_train_labels):
    
    print('-------------------{}-------------------'.format(fold_var))

    #************************************
    #imprime os dados que serão treinados e validados
    '''
    print('Linhas de treino e validação\n')
    print('Treino:',train_index)
    print('Validação:', val_index)
    print('\n')
    '''
    #print('Treino: %s, Validação: %s' % (data_train_labels[train_index], data_train_labels[val_index]))
    
    #************************************


    #pegando os valores que vão ser treinados e validados 
    #treinamento_data, validacao_data = data_train_labels.iloc[train_index], data_train_labels.iloc[val_index]
    #treino
    treinamento_data, validacao_data = data_train_labels[train_index], data_train_labels[val_index]

    #teste ??


    #************************************

    #mostrando os valores que vão ser treinados e validados     
    #print(treinamento_data.head())
    #print(treinamento_data)
    #print(validacao_data)  
    #************************************
    
    
    #Instanciando o modelo VGG16
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

    #compilando o model
    model.compile(
        loss='binary_crossentropy',#usar esse loss?
        optimizer=adam,
        metrics=['accuracy'])

    treinamento_data = keras.preprocessing.image.ImageDataGenerator(
        preprocessing_function=keras.applications.vgg16.preprocess_input,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    validacao_data = keras.preprocessing.image.ImageDataGenerator(
        preprocessing_function= keras.applications.vgg16.preprocess_input,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

    train_data = treinamento_data.flow_from_directory(
      train,
      target_size = (224, 224),
      batch_size = 2,
      class_mode = 'categorical')

    #validação (mudar)
    test_data = validacao_data.flow_from_directory(
      test,
      target_size = (224, 224),
      batch_size = 2,
      class_mode = 'categorical')

    '''
    checkpoint = keras.callbacks.ModelCheckpoint(
      filepath='mymodel.h5',
      verbose=2,
      save_best_only=True)
    '''

    checkpoint = keras.callbacks.ModelCheckpoint(
        image_dir+get_model_name(fold_var),
        monitor = 'val_accuracy',
        verbose = 1,
        save_best_only = True, 
        mode = 'max'
    )


    callbacks = [checkpoint]

    start = datetime.datetime.now()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO da Parte de Treinamento >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    model_history = model.fit_generator(
      train_data,
      validation_data = test_data,
      epochs = 10,
      steps_per_epoch=5,
      validation_steps=32,
      callbacks=callbacks ,verbose=2)


    #selecionando o melhor modelo
    model.load_weights("/image_dir/model_"+str(fold_var)+".h5")

    results = model.evaluate(test_data)
    results = dict(zip(model.metrics_names, results))

    VALI_ACURACIA.append(results['accuracy'])
    VALI_LOSS.append(results

    
    clear_session()

    fold_var +=1 




    '''
    duration = datetime.datetime.now() - start
    print("Duração do treinamento da rede:\n", duration)
    '''                                        

    '''
    print('Acuracia do modelo:\n')
    print(model_history.history['accuracy'])
    '''
    
    '''
    #gráfico 
    plt.plot(model_history.history['accuracy'])
    plt.title('CNN Model accuracy values')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show() 
    '''

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FIM da Parte de Treinamento >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>








'''
  #Instanciando o modelo VGG16
  vgg = keras.applications.vgg16.VGG16( input_shape= IMAGE_SIZE + [3], 
                                        weights='imagenet', #pesos pré-treinados do imagenet (transfer-learning workflow)
                                        include_top=False)

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

  #***************************
  
  train_data_generator = idg.flow_from_dataframe( treinamento_data,
                                                  directory= image_dir,
                                                  #x_col = "filename", 
                                                  #y_col = "label",
                                                  class_mode = "categorical", 
                                                  shuffle = True)
  
  valid_data_generator= idg.flow_from_dataframe(validacao_data,
                                                directory= image_dir,
                                                #x_col = "filename", 
                                                #y_col = "label",
                                                class_mode = "categorical", 
                                                shuffle = True)

  #+++++++++++++++++++++++++++++++++++++



  #compilando o model
  model.compile(loss = 'categorical_crossentropy',
                optimizer = opt,
                metrics = ['accuracy'])

  checkpoint = keras.callbacks.ModelCheckpoint( save_dir+get_model_name(fold_var),
                                                monitor='val_accuracy',
                                                verbose=1, 
                                                save_best_only=True,
                                                mode = 'max')

  callbacks = [checkpoint]
  
  #treinando a rede

  model_history = model.fit(validacao_data,
                            validation_data = treinamento_data, #test_set
                            epochs = 10,
                            steps_per_epoch = 5,
                            validation_steps = 32,
                            callbacks = callbacks,
                            verbose=2)

  #Salvando o model
  model.load_weights("/saved_models/model"+str(fold_var)+".h5")

  results = model.evaluate(valid_data_generator)
  results = dict(zip(model.metrics_names, results))

  VALI_ACURACIA.append(results['accuracy'])
  VALI_LOSS.append(results['loss'])

  tf.keras.backend.clear_session()
  fold_var += 1


#**********************FIM DO TESTE (COMPILANDO COM KFOLD)************************
'''








