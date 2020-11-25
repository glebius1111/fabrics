import argparse

import cv2
import os
import image
from scipy.spatial import distance as dist
import matplotlib.image as mpimg
import numpy
from operator import attrgetter
hog_descriptor = cv2.HOGDescriptor((64, 64), (32, 32), (16, 16), (8, 8,), 12)
imobj = []
folder = 'africa_fabric'
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, filename))
    obj = image.Image(img, hog_descriptor)
    imobj.append(obj)
newimg = image.Image(cv2.imread('new.jpg'), hog_descriptor)
# for im in imobj:
#     im.hogdist = (dist.euclidean(imobj[0].data, im.data))
# imobj = sorted(imobj, key=attrgetter("hogdist"))
# cv2.imshow("image", imobj[0].img)
# cv2.waitKey(0)
#
# cv2.imshow("image", imobj[1].img)
# cv2.waitKey(0)
comp = (255- imobj[0].img)
for im in imobj:
    im.colordist = (dist.euclidean(comp.reshape(12288), im.img.reshape(12288)))
imobj = sorted(imobj, key=attrgetter("colordist"))
cv2.imshow("image1", comp)
cv2.waitKey(0)

cv2.imshow("image", imobj[0].img)
cv2.waitKey(0)