import tensorflow as tf 
from tensorflow import keras
Epocas               = 50
import numpy as np 
import os
import random
import cv2 as cv
import matplotlib.pyplot as plt

teste2 = 'C:\\Users\\heloh\\Desktop\\testeCNN\\teste2'
teste = 'C:\\Users\\heloh\\Desktop\\testeCNN\\train\\teste' #não está usando

treino_M = 'C:\\Users\\heloh\\Desktop\\testeCNN\\train\\M' #maligno
treino_B = 'C:\\Users\\heloh\\Desktop\\testeCNN\\train\\B' #benigno
treino_N =  'C:\\Users\\heloh\\Desktop\\testeCNN\\train\\Normal' #benigno

#pegando todas as fotos 
treino_M = ['C:\\Users\\heloh\\Desktop\\testeCNN\\train\\M\\{}'.format(i) for i in os.listdir(treino_M)]  #maligno
treino_B = ['C:\\Users\\heloh\\Desktop\\testeCNN\\train\\B\\{}'.format(i) for i in os.listdir(treino_B)]  #benigno

treino_N = ['C:\\Users\\heloh\\Desktop\\testeCNN\\train\\Normal\\{}'.format(i) for i in os.listdir(treino_N)]  #normal

teste_imagens = ['C:\\Users\\heloh\\Desktop\\testeCNN\\train\\teste\\{}'.format(i) for i in os.listdir(teste)] #teste

#redimencionando as imagens 150 x 150
linhas = 224 #quantidade de linhas
colunas = 224 #quantidade de colunas
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

print('teste')
print(treino_imagens.shape)
print(treino_labels.shape)


IMAGE_SIZE = [224, 224]

#****************************************************
#vgg = keras.applications.vgg16.VGG16(input_shape= IMAGE_SIZE + [3], weights=None, include_top=False)
vgg = keras.applications.vgg16.VGG16(input_shape= IMAGE_SIZE + [3], weights='imagenet', include_top=False)
#vgg = keras.applications.vgg16.VGG16(weights='imagenet', include_top=False)

vgg.input

for layer in vgg.layers:
  layer.trainable = False

import glob

folders = glob. glob('C:\\Users\\heloh\\Desktop\\testeCNN\\train\\teste\\*')
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

train_set = train_datagen.flow_from_directory(teste,
                                                 target_size = (224, 224),
                                                 batch_size = 2,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory(teste2,
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

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INICIO da Parte de Treinamento
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> FIM da Parte de Treinamento
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



#********

img = keras.preprocessing.image.load_img("mdb092.PNG",target_size=(224,224))
img = np.asarray(img)
plt.imshow(img)
img = np.expand_dims(img, axis=0)


saved_model = keras.models.load_model("mymodel.h5")
#output = saved_model.predict(img) #
output = model.predict(img)

print('output')
#print(output)


#****

#label = keras.applications.vgg16.decode_predictions(output, top =1)
#print(label)

#label = keras.applications.vgg16.decode_predictions(output)

#label = label[0][0]

#print('%s (%.2f%%)' % (label[1], label[2]*100))

#****

if output[0][0] > output[0][1]:
    print("Maligno")
    print(prediction )
    print(layer)
    print(folders)
    print(model)

else:
    print('Benigno')




'''
def read_and_process_image(list_of_images):
    """
    Returns two arrays: 
        X is an array of resized images
        y is an array of labels
    """
    X = [] # images
    y = [] # labels
    
    for image in list_of_images:
        X.append(cv.resize(cv.imread(image, cv.IMREAD_COLOR), (224,224), interpolation=cv.INTER_CUBIC))  #Read the image
        #get the labels
        if 'm' in image:
            y.append(1)
        elif 'cat' in image:
            y.append(0)

    return X, y


#**********************************

model= keras.models.load_model('mymodel.h5')
test_imgs = ['C:\\Users\\heloh\\Desktop\\testeCNN\\teste2\\{}'.format(i) for i in os.listdir(teste2)]

TirarFoto=False
ImagensParaAvaliar = 1


if (TirarFoto==False):
    #Now lets predict on the first ImagensParaAvaliar of the test set
    X_test, y_test = read_and_process_image(test_imgs[0:ImagensParaAvaliar]) #Y_test in this case will be empty.
    x = np.array(X_test)
    test_datagen = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
    i = 0
    text_labels = []
    plt.figure(figsize=(20,20))
    
    for batch in test_datagen.flow(x, batch_size=1):
        pred = model.predict(batch)
        if pred > 0.5:
            text_labels.append(f'benigno {pred}')
        else:
            text_labels.append(f'Gamalignoto {pred}')
        #Número de linhas, número de colunas
        plt.subplot((ImagensParaAvaliar / 224) + 1, 224, i + 1)
        plt.title('' + text_labels[i])
        imgplot = plt.imshow(batch[0])
        i += 1
        if i % ImagensParaAvaliar == 0:
            break
    plt.show()
'''
