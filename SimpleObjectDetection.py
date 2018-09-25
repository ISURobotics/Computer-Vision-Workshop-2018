import cv2 # Import OpenCV so we can use it!
import numpy as np # Numpy is a handy package to work with matrices

"""
This program extends on the thresholding functionality for simple object detection!
We explore OpenCV's contour detection functionality to draw a box around our biggest
object of the proper color.
"""

imgWidth = 640
imgHeight = 480

def nothing(x): # Don't worry about this, it literally doesn't do anything.
    pass

cv2.namedWindow('image')  # Create a window to display the image

# Create three "trackbars" that will let us change variables based on sliding a trackbar!
cv2.createTrackbar("Hue Lower", 'image', 0, 255, nothing)
cv2.createTrackbar("Hue Upper", 'image', 0, 255, nothing)
cv2.createTrackbar("Hue Center", 'image', 0, 255, nothing)

#We'll initialize the trackbars to allow every color to pass through.
hueLower = 0
hueUpper = 255
hueCenter = 127
cv2.setTrackbarPos('Hue Lower', 'image', hueLower)
cv2.setTrackbarPos('Hue Upper', 'image', hueUpper)
cv2.setTrackbarPos('Hue Center', 'image', hueCenter)

cap = cv2.VideoCapture(0) # Create a webcam object called cap (Short for capture)
cap.set(3, imgWidth) # Set the camera resolution, these are optional
cap.set(4, imgHeight)

#Let's loop forever!
while True:
    ret, frame = cap.read() # Read an image from the webcam

    # After we read an image, let's be sure we update our variables from the trackbar.
    hueLower = cv2.getTrackbarPos('Hue Lower', 'image')
    hueUpper = cv2.getTrackbarPos('Hue Upper', 'image')

    #This little chunk of code just exists for convenience.  It'll let us slide the hue range around.
    if(hueCenter != cv2.getTrackbarPos('Hue Center', 'image')):
        difference = cv2.getTrackbarPos('Hue Center', 'image') - hueCenter
        hueLower = hueLower + difference
        hueUpper = hueUpper + difference
        hueCenter = cv2.getTrackbarPos('Hue Center', 'image')
    cv2.setTrackbarPos('Hue Lower', 'image', hueLower)
    cv2.setTrackbarPos('Hue Upper', 'image', hueUpper)
    cv2.setTrackbarPos('Hue Center', 'image', hueCenter)

    """
    Okay, here's the fun stuff!
    First off, we convert our webcam frame to the HSV color space.
    HSV is short for Hue, Saturation, Value.  Think of it like color, how saturated is the color, and how bright it is.
    We then create a mask of all values in frameHSV that are within the hue bounds we set.
    The cv2.inRange() function asks for a lower bound and upper bound.  Because we've arbitrarily decided to threshold
    based on hue, we can set saturation and value to be any value between 0-255.  It returns a black and white only
    image that says "yep this part is in the right range!" or "nope, not in the right range".
    Erode and dilate are used to "de-noise" the mask and make it a little smoother.
    We then create maskedFrame.  This is the original image cropped to wherever the mask was "true"
    """
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV, (hueLower, 0, 0), (hueUpper, 255, 255))
    mask = cv2.erode(mask, None, iterations=1)  # Filters out noise in the image to get a better mask
    mask = cv2.dilate(mask, None, iterations=2)
    maskedFrame = cv2.bitwise_and(frame, frame, mask=mask)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]  # makes an object (cnts, short for contours) that stores the locations of all boundaries in the mask.
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        print("Found something!")
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (
        int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))  # a bit advanced, but it finds the center of the circle.

        # only proceed if the radius meets a minimum size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(maskedFrame, (int(x), int(y)), int(radius), (0, 255, 255), 4)  # Draw the circle.
            cv2.circle(maskedFrame, center, 5, (0, 0, 255), -1)  # Make a dot on the center.

    #Now let's display the mask and the maskedImage with the drawn circle!
    cv2.imshow('image', maskedFrame)
    cv2.imshow('mask', mask)

    #If you press q, break from the while loop
    key = cv2.waitKey(1)
    if key == ord('q'):
        break



