from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import cv2

#Let's load a pre-trained model from Keras!
model = ResNet50(weights='imagenet')

#Set up the webcam as usual
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

#Let's loop forever again
while True:
    ret, img = cap.read() # Get an image from the webcam
    # The neural network expects a square input, so let's just crop the center of our image
    # This is done using numpy array slicing! An image is simply a numpy array.
    cropped = img.copy()[0:720, 280:1000]

    # The network wants a 224x224 image, so we'll resize our square image.
    cropped = cv2.resize(cropped, (224, 224))

    # This is some preprocesssing to ensure the data is in the correct format for the neural network
    x = image.img_to_array(cropped.copy())
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    # This line makes predictions!!
    preds = model.predict(x)

    # Now we just interpret those predictions based on the original network architecture.
    prediction = decode_predictions(preds, top=1)[0]
    confidence = prediction[0][2]
    className = prediction[0][1]

    # We can print the results for some easy analysis.
    if (confidence > .5):
        print("Class, confidence: " + className + ", " + str(confidence))

    # And we'll show the image for good measure
    cv2.imshow("Image Cropped", cropped)
    cv2.waitKey(1)