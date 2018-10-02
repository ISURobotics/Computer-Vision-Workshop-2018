# Computer-Vision-Workshop-2018
Thanks for the interest in the 2018 ISU Robotics Club Computer Vision Workshop!  The workshop will be hosted the evening of October 2nd at 6:30 PM in Carver 205.  Prior to coming, please follow the following installation guide so we can jump right in during the workshop!

# Installation on Windows
For Mac and Ubuntu, see further down.

  1.  Download and install Anaconda: https://www.anaconda.com/download/
  You'll want to download the Python 3.6, 64 bit version.  If it gives you the option to "Add Anaconda to my PATH environment variable", check the box despite it saying not recommended.
  
  2.  After Anaconda is installed, open your command prompt and type:
  ```
  conda update conda
  conda update --all
  ```
  3.  Now you'll want to create a conda environment so you can install OpenCV in it!  In your command prompt, type the following:
  ```
  conda create -n CVWorkshop python=3.5 numpy scipy matplotlib
  ```
  4.  After that's done, type:
  ```
  activate CVWorkshop
  ```
  At this point, you're in a virtual environment named CVWorkshop with Python version 3.5, and the packages numpy, scipy, and matplotlib installed.  Next up is installing OpenCV!
  
  5.  To install OpenCV with Anaconda, still within the same command prompt as before, type this:
  ```
  conda install -c conda-forge opencv
  ```
  6.  To test your installation of OpenCV, we're going to first start up the Python shell and import OpenCV:
  ```
  python
  import cv2
  ```
  Nothing should happen... If you get an error, send a message via Slack and we'll get it figured out!
  
  7.  Exit the Python shell by typing exit().  Be sure you're still in your virtual environment.  Now we're going to install tensorflow.  For the purposes of this workshop, we'll be doing it without GPU support to simplify installation.  Simply type:
  ```
  pip install tensorflow
  ```
  8.  Next we're installing Keras, a high level deep learning framework.  Type:
  ```
  pip install keras
  ```
  At this point, we should have OpenCV, Tensorflow, and Keras installed in our Python 3.5 Anaconda Environment.  Please confirm this by entering your Python shell by typing "python", then typing the following:
  ```
  import cv2
  import tensorflow as tf
  import keras
  ```
  You should see "Using Tensorflow Backend".
  
  
 # Installation on Mac
 Follow this guide to install OpenCV on your Mac: https://medium.com/init27-labs/installation-of-opencv-using-anaconda-mac-faded05a4ef6.  Use step 4b rather than 4a and rather than python=2.7, type python=3.5. **NOTE:** During step 4b use 'conda install -c conda-forge matplotlib' instead of 'conda install -c conda- forge matplotlib'. After OpenCV is installed, follow these steps:
  1.  Install tensorflow.  Start by activating your new Anaconda environment by typing:
  ```
  source activate CVWorkshop
  ```
  Be sure to switch "CVWorkshop" with whatever you named your environment.  Then type:
  ```
  pip install tensorflow
  ```
  
  2.  Install Keras, which is our high-level deep learning framework. Type:
  ```
  pip install keras
  ```
 At this point, we should have OpenCV, Tensorflow, and Keras installed in our Python 3.5 Anaconda Environment.  Please confirm this by entering your Python shell by typing "python", then typing the following:
  ```
  import cv2
  import tensorflow as tf
  import keras
  ```
  You should see "Using Tensorflow Backend".
  
 # Installation on Ubuntu
  1.  Start off by following this tutorial to install Anaconda: https://www.digitalocean.com/community/tutorials/how-to-install-the-anaconda-python-distribution-on-ubuntu-16-04
  2.  Follow the steps in the Windows installation guide.
  
