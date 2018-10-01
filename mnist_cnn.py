'''Trains a simple convnet on the MNIST dataset.
Gets to 99.25% test accuracy after 12 epochs
(there is still a lot of margin for parameter tuning).
16 seconds per epoch on a GRID K520 GPU.
'''

# This code is from here: https://github.com/keras-team/keras/blob/master/examples/mnist_cnn.py
# It is modified to include comments for the ISURC Computer Vision Workshop

from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

batch_size = 128 # How many images to use to update weights one time
num_classes = 10 # How many classes we want to classify
epochs = 12 # How many times to iterate through all the data

# input image dimensions
img_rows, img_cols = 28, 28

# the data, split between train and test sets
# We do this to prevent overfitting.
# We don't want the model to just learn literally ONLY this dataset!
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# This is specific to Keras, don't worry about it for now.
if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

# Let's modify our data to be floating point numbers rather than an 8-bit unsigned int
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
# As an example, 3 might be converted to:
# [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)


#Below is where we define model architecture!
model = Sequential() # The layers are stacked sequentially.  Ask me about the functional API if you want!
model.add(Conv2D(32, kernel_size=(3, 3), # We'll have 32 3x3 filters with RANDOM weights to start
                 activation='relu', # This is our non-linear activation function so we can take advantage of multiple layers
                 input_shape=input_shape)) # Keras handles this automatically for other layers
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2))) # A non-linear filter that takes the max of each 2x2 block.
model.add(Dropout(0.25)) # Helps prevent overfitting by randomly excluding 25% of neurons during an epoch
model.add(Flatten()) # a 3x3 matrix will beoome a 1x9 vector.
model.add(Dense(128, activation='relu')) # Now we look for all possible combinations of features and how they fit together
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax')) # We have one last dense connected layer with each of our outputs! Softmax acts as a probability.

#We compile the model now so we can train it.
model.compile(loss=keras.losses.categorical_crossentropy, # Categorical crossentropy is what we want to minimize
              optimizer=keras.optimizers.Adadelta(), # We'll modify the learning rate as we go
              metrics=['accuracy'])

# Now we train the model with our training datasets! We test it with the test datasets.
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
# We could also save the model weights for use later.  In the next example we'll see what that looks like in real time.
print('Test loss:', score[0])
print('Test accuracy:', score[1])