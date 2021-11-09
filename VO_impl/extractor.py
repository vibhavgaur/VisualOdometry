import cv2
import numpy as np
from skimage.measure import ransac
from skimage.transform import FundamentalMatrixTransform


class Extractor():
    # for matching features between frames
    def __init__(self):
        self.lastFrame = None
        self.detector = cv2.ORB_create()
        self.matcher = cv2.BFMatcher(cv2.NORM_HAMMING)#, crossCheck = True)

    def detectFeatures(self, img):
        goodFeats = cv2.goodFeaturesToTrack(np.mean(img, axis = 2, dtype = np.uint8), maxCorners = 1000, qualityLevel = 0.01, minDistance = 3)
        kps = [cv2.KeyPoint(x = f[0][0], y = f[0][1], _size = 20) for f in goodFeats]
        return kps

    def matchFeatures(self, img, kps):
        # compute descriptors
        kps, des = self.detector.compute(img, kps)
        if self.lastFrame is not None:
            # match features between this and last frame
            matches = self.matcher.knnMatch(des, self.lastFrame['des'], k = 2)
            # applying ratio test
            goodMatches = [m for m, n in matches if m.distance < 0.75*n.distance]
            # Filtering matches using Fundamental Matrix Transform
            ransacData = np.array([(kps[m.queryIdx].pt, kps[m.queryIdx].pt) for m in goodMatches])
            F, inliers = ransac((ransacData[:,0], ransacData[:,1]), FundamentalMatrixTransform, min_samples=8, residual_threshold=1, max_trials=2000)
            print("Fundamental Matrix:\n", F.params)

        # update last frame's properties
        self.lastFrame = {'kps':kps, 'des':des}
