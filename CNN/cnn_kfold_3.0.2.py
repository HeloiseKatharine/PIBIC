# fontes:
# https://github.com/jeffheaton/t81_558_deep_learning/blob/master/t81_558_class_05_2_kfold.ipynb
# https://medium.com/the-owl/k-fold-cross-validation-in-keras-3ec4a3a00538
# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html
# https://www.dobitaobyte.com.br/como-criar-um-dataset-para-deep-learning/
# https://www.pyimagesearch.com/2018/05/07/multi-label-classification-with-keras/ 
# https://vijayabhaskar96.medium.com/multi-label-image-classification-tutorial-with-keras-imagedatagenerator-cd541f8eaf24
# https://keras.io/api/applications/vgg/#vgg16-function
# https://keras.io/guides/transfer_learning/

from os import P_NOWAIT
from sklearn.utils.validation import check_random_state
import tensorflow as tf 
from tensorflow import keras
import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt
import datetime
from sklearn.model_selection import KFold, StratifiedKFold 

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

#labels data_train

data_train_labels = []

print('********TESTE**********')


for i in treino_B:
  data_train_labels.append(0)# benigno = 0 maligno = 1

for i in treino_M:
  data_train_labels.append(1)# benigno = 0 maligno = 1

#**********************************************
print(data_train_labels)
print(len(treino_B))
print(len(treino_M))
print(len(data_train_labels))
#**********************************************


data_train = treino_B + treino_M #benigno e maligno 



#**********************************************
print('********TESTE**********')

for i in range(len(data_train)):
  print(data_train[i])

print(len(data_train))
print('********TESTE**********')





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO da validação cruzada >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#**********************************************


#validação cruzada

Y = data_train_labels

kf = KFold(n_splits = 5)
#TESTAR LOGO 
kf = StratifiedKFold(n_split = 5, random_state = 7, shuffle = True)


idg = keras.preprocessing.image.ImageDataGenerator (width_shift_range= 0.1,
                          height_shift_range= 0.1,
                          zoom_range= 3.0,
                          fill_mode= 'nearest',
                          horizontal_flip= True,
                          rescale= 1./224) 

def get_model_name(k):
  return 'model_'+str(k)+'.h5'

vali_acuracia = []
vali_loss = []

salve_dir = '/saved_models/'
fold_var = 1


#**********************************************

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FIM da validação cruzada >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#Instanciando o modelo VGG16
vgg = keras.applications.vgg16.VGG16(
    input_shape= IMAGE_SIZE + [3], 
    weights='imagenet', #pesos pré-treinados do imagenet (transfer-learning workflow)
    include_top=False
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


train_set = train_datagen.flow_from_directory(
    train,
    target_size = (224, 224),
    batch_size = 2,
    class_mode = 'categorical'
    )

test_set = test_datagen.flow_from_directory(
    test,
    target_size = (224, 224),
    batch_size = 2,
    class_mode = 'categorical'
    )


checkpoint = keras.callbacks.ModelCheckpoint(filepath='mymodel2.h5',
  verbose=2, 
  save_best_only=True
  )

callbacks = [checkpoint]

start = datetime.datetime.now()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO da Parte de Treinamento >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''
model_history=model.fit_generator(
  train_set,
  validation_data=test_set,
  epochs=10,
  steps_per_epoch=5,
  validation_steps=32,
  callbacks=callbacks ,verbose=2)


duration = datetime.datetime.now() - start
print("Duração do treinamento da rede: ", duration)                                          


#gráfico 
#############################
print('Qual é a acuracia do modelo ?')
print(model_history.history['accuracy'])

plt.plot(model_history.history['accuracy'])
plt.title('CNN Model accuracy values')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
'''
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FIM da Parte de Treinamento >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TESTANDO A REDE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

img = keras.preprocessing.image.load_img("mdb092.PNG",target_size=(224,224)) #M
img = np.asarray(img)
plt.imshow(img)
img = np.expand_dims(img, axis=0)

saved_model = keras.models.load_model("mymodel2.h5")
output = model.predict(img)

print('output')
print(output)

predictions = model.predict_generator(img)
print('predictions')
print(predictions)
argmax = np.argmax(predictions)
print(np.argmax(predictions))

print("**************************************")

# benigno = 0 maligno = 1

if(argmax == 0):
    print('Benigno')

if(argmax == 1):
     print("Maligno")
