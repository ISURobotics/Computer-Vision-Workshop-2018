# Computer-Vision-Workshop-2018
Thanks for the interest in the 2018 ISU Robotics Club Computer Vision Workshop!  The workshop will be hosted the evening of October 2nd at 6:30 PM, room TBA.  Prior to coming, please follow the following installation guide so we can jump right in during the workshop!

# Installation
First off, I'm making the assumption you're using a Windows 10 PC.  If you have a Mac, you'll need to download the macOS version of Anaconda.

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
  
 # Preparing for the Workshop
 Absolutely no programming experience is required to attend this workshop, but a bit of preparation is requested!  Aside from installing OpenCV, please take the time to ensure you have a working webcam.  It can be built in to your laptop or a USB one, doesn't make a difference!  I'd also like you to print out this checkerboard and bring it with you: https://docs.opencv.org/2.4/_downloads/pattern.png
