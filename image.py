import cv2
from scipy.spatial import distance as dist
import numpy as np
class Image:
    def __init__(self, img, hog):
        self.img = img
#        self.data = cv2.calcHist([img], [0, 1, 2], None, [64, 64, 64], [0, 256, 0, 256, 0, 256])
        self.data = hog.compute(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY ) )
