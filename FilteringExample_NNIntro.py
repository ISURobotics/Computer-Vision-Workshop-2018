import cv2
import numpy as np

"""
This is just a demo script describing what filters are and how they act on an image.
Filters are, in a sense, the basis of all neural networks.
Another word for a filter is a kernel.
"""

#Initialize our webcam and get a single frame
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

#Convert the image to grayscale
img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#Okay, here is where we define a couple filters:
#We created a corner detector, horizontal edge detector, and vertical edge detector
cornerFilter = -1*np.array(([-1, -1, 0, 0], [-1, -1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]), dtype = np.float32)
horizontalEdgeFilter = np.array([[-1, -1], [0, 0], [1, 1]], dtype=np.float32)
verticalEdgeFilter = np.array([[-1, 0, 1], [-1, 0, 1]], dtype = np.float32)

#Now let's perform the 2D convolution...
filteredCornerImage = cv2.filter2D(img.copy(), -1, cornerFilter)
horizEdge = cv2.filter2D(img.copy(), -1, horizontalEdgeFilter)
vertEdge = cv2.filter2D(img.copy(), -1, verticalEdgeFilter)

#Here's the results!
cv2.imshow("corner", img)
cv2.imshow("Filter response", filteredCornerImage)
cv2.imshow("Vertical Edge", vertEdge)
cv2.imshow("Horizontal Edge", horizEdge)
cv2.waitKey(0)
