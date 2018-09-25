import cv2
import numpy as np

cameraMatrix1 = np.array([[699.555, 0, 658.919],[0, 699.555, 360.179], [0, 0, 1]])
cameraMatrix2 = np.array([[700.535, 0, 630.414], [0, 700.535, 357.362], [0, 0, 1]])
distCoeffs1 = np.array([-.16912, .021884, 0, 0])
distCoeffs2 = np.array([-.17153, .0024183, 0, 0])
imageSize = (1280, 720)
R = np.eye(3,3)
T = np.array([.12, 0, 0])

rotation1, rotation2, pose1, pose2, Q, roi1, roi2 = cv2.stereoRectify(cameraMatrix1=cameraMatrix1, distCoeffs1=distCoeffs1, cameraMatrix2=cameraMatrix2, distCoeffs2=distCoeffs2, imageSize=imageSize, R = R, T = T)
map1x, map1y = cv2.initUndistortRectifyMap(cameraMatrix1, distCoeffs1, rotation1, pose1, (1280,720), cv2.CV_32FC1)
map2x, map2y = cv2.initUndistortRectifyMap(cameraMatrix2, distCoeffs2, rotation2, pose2, (1280,720), cv2.CV_32FC1)

cap = cv2.VideoCapture(1)
cap.set(3, 2560)
cap.set(4, 720)
while True:
    ret, img = cap.read()

    imgL = img[:, :1280, :]
    imgR = img[:, -1280:, :]

    imgLRect = np.rot90(cv2.remap(imgL, map1x, map1y, interpolation=0), k=2, axes=(0,1)).astype(np.uint8)
    imgRRect = np.rot90(cv2.remap(imgR, map2x, map2y, interpolation=0), k=2, axes=(0,1)).astype(np.uint8)

    imgLRect = cv2.cvtColor(imgLRect, cv2.COLOR_BGR2GRAY)
    imgRRect = cv2.cvtColor(imgRRect, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Left", imgLRect)
    # cv2.imshow("Right", imgRRect)
    stereo = cv2.StereoSGBM_create(minDisparity=0, numDisparities=80, blockSize=5, uniquenessRatio=15, speckleWindowSize=20, speckleRange=50)
    disp16 = stereo.compute(imgLRect, imgRRect)
    # print(np.amax(disp16))
    # disp = np.zeros((720, 1280))
    # cv2.normalize(disp16, disp, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    disp = (disp16/4).astype(np.uint8)
    disp[disp>250] = 0
    cv2.imshow("disparity", disp)


    key = cv2.waitKey(1)
    if key == ord('q'):
        break
