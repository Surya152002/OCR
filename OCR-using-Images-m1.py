from PIL import Image
import pyTesseract
import numpy as np
filename = 'image_01.png'
img1 = np.array(Image.open(filename))
text = pyTesseract.image_to_string(img1)
print(text)
filename = 'image_02.png'
img2 = np.array(Image.open(filename))
text = pyTesseract.image_to_string(img2)
print(text)
import numpy as np
import cv2norm_img = np.zeros((img.shape[0], img.shape[1]))
img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
img = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
img = cv2.GaussianBlur(img, (1, 1), 0)
