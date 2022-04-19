from PIL import Image
import numpy as np

im = np.array(Image.open('a.png'))

print(im.shape)

print(im[100, 150])

print(type(im[100, 150]))
# <class 'numpy.ndarray'>