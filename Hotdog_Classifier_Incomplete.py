import cv2
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import os
import random
import numpy as np


random.seed(1)

batch_size = 10 # How many images to use to update weights one time
num_classes = 2 # How many classes we want to classify
epochs = 15 # How many times to iterate through all the data

img_rows = 100
img_cols = 100

X_Train = []
Y_Train = []
X_Test = []
Y_Test = []

datasetPath = "dataset"

#I have only provided code to load the dataset.  You design the model, compile it, and train it!
for folder in os.listdir(datasetPath):
    for file in os.listdir(os.path.join(datasetPath, folder)):
        randNum = random.random()
        filename = os.path.join(datasetPath, folder, file)
        tempImg = cv2.imread(filename)
        tempImg = cv2.resize(tempImg, (img_rows, img_cols))
        if folder=='hotdog':
            label = 1
        else:
            label = 0
        if(randNum < .75):
            X_Train.append(tempImg)
            Y_Train.append(label)
        else:
            X_Test.append(tempImg)
            Y_Test.append(label)

X_Train = np.array(X_Train).astype(np.float32)/255.0
X_Test = np.array(X_Test).astype(np.float32)/255.0
Y_Train = np.array(Y_Train).astype(np.float32)
Y_Test = np.array(Y_Test).astype(np.float32)

Y_Train = keras.utils.to_categorical(Y_Train, num_classes)
Y_Test = keras.utils.to_categorical(Y_Test, num_classes)

input_shape = (img_rows, img_cols, 3)

#Design your model here!

#model.save('Hotdog.h5')



