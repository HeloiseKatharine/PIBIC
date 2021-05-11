import tensorflow as tf 
from tensorflow import keras
#Epocas               = 50
import numpy as np 
import os
import random
import cv2 as cv
import matplotlib.pyplot as plt

#localização das pastas do teste e do treino
test = 'D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\test' 
train = 'D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train'


#APAGAR
#redimencionando as imagens 150 x 150
linhas = 224 #quantidade de linhas
colunas = 224 #quantidade de colunas
channels = 1  #1 = tons cinza


#retorna uma lista com as imagens redimencionadas e uma lista com as labels


IMAGE_SIZE = [224, 224]

#****************************************************
#vgg = keras.applications.vgg16.VGG16(input_shape= IMAGE_SIZE + [3], weights=None, include_top=False)
vgg = keras.applications.vgg16.VGG16(input_shape= IMAGE_SIZE + [3], weights='imagenet', include_top=False)
#vgg = keras.applications.vgg16.VGG16(weights='imagenet', include_top=False)

#vgg.input
vgg.output

for layer in vgg.layers:
  layer.trainable = False

import glob

folders = glob. glob('D:\\heloh\\Documents\\MeuRepositorio\\PIBIC\\CNN\\train\\*') #pasta de treino
print(len(folders))


x = keras.layers.Flatten()(vgg.output)
prediction = keras.layers.Dense(len(folders), activation='softmax')(x)
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


'''
tf.keras.callbacks.ModelCheckpoint(
    filepath, monitor='val_loss', verbose=0, save_best_only=False,
    save_weights_only=False, mode='auto', save_freq='epoch',
    options=None, **kwargs
)

'''
checkpoint = keras.callbacks.ModelCheckpoint(filepath='mymodel.h5',
                               verbose=2, save_best_only=True)

#checkpoint = keras.callbacks.ModelCheckpoint(filepath='mymodel.h5',
#                               verbose=2, save_best_only=False, save_freq='epoch')

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
print("Training completed in time: ", duration)                                          



# Plot training & validation loss values
plt.plot(model_history.history['accuracy'])
#plt.plot(model_history.history['val_accuracy'])
plt.title('CNN Model accuracy values')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
'''

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FIM da Parte de Treinamento >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Incio do teste >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


img = keras.preprocessing.image.load_img("mdb092.PNG",target_size=(224,224)) #M
img = np.asarray(img)
plt.imshow(img)
img = np.expand_dims(img, axis=0)


saved_model = keras.models.load_model("mymodel.h5")
#output = saved_model.predict(img) 
output = model.predict(img)

print(output)


class_names = sorted(train_set.class_indices.items(), key = lambda pair:pair[1])

print(class_names)

predict_res = model.predict_generator(img)
predict_id = np.argmax(predict_res)
predict_label = class_names[predict_id]

#print(predict_label)
print(predict_label[0])
#print(predict_label[1])

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FIM do teste >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#APAGAR 

#****

#label = keras.applications.vgg16.decode_predictions(output, top =1)
#print(label)

#label = keras.applications.vgg16.decode_predictions(output)

#label = label[0][0]

#print('%s (%.2f%%)' % (label[1], label[2]*100))

#****

'''

if output[0][0] > output[0][1]:
    print("Maligno")
    print(prediction )
    print(layer)
    print(folders)
    print(model)

else:
    print('Benigno')
''' 

#predict_res = model.predict_generator(img)
#print(predict_res)

