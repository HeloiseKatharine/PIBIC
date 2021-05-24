import tensorflow as tf 
from tensorflow import keras
import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt

#localização das pastas do teste e do treino
train = 'D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train'
test = 'D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\test' 

#APAGAR
#redimencionando as imagens 150 x 150
linhas = 224 #quantidade de linhas
colunas = 224 #quantidade de colunas
channels = 1  #1 = tons cinza

IMAGE_SIZE = [224, 224]

#VGG16
vgg = keras.applications.vgg16.VGG16(input_shape= IMAGE_SIZE + [3], weights='imagenet', include_top=False)

#vgg.input
vgg.output

for layer in vgg.layers:
  layer.trainable = False

x = keras.layers.Flatten()(vgg.output)
prediction = keras.layers.Dense(2, activation='softmax')(x) #duas classes
model = keras.Model(inputs=vgg.input, outputs=prediction)
model.summary()

adam = keras.optimizers.Adam()

model.compile(loss='binary_crossentropy',
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

train_set = train_datagen.flow_from_directory(train,
                                                 target_size = (224, 224),
                                                 batch_size = 2,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory(test,
                                            target_size = (224, 224),
                                            batch_size = 2,
                                            class_mode = 'categorical')

import datetime

checkpoint = keras.callbacks.ModelCheckpoint(filepath='mymodel.h5',
                               verbose=2, save_best_only=True)

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

saved_model = keras.models.load_model("mymodel.h5")
output = model.predict(img)

print(output)

class_names = sorted(train_set.class_indices.items(), key = lambda pair:pair[1])
predict = model.predict_generator(img)
argmax = np.argmax(predict)
class_name = class_names[argmax]
#print(class_names)

if(argmax == 0):
    print('Benigno')


if(argmax == 1):
     print("Maligno")

print(predict)
print(argmax )
print(class_name)