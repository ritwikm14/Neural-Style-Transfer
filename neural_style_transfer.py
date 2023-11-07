# -*- coding: utf-8 -*-
"""Neural Style Transfer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x0-zbmpGPr11ILTZvD2wq-8JhMP99_iu
"""

!pip install tensorflow
!pip install tensorflow_hub

import tensorflow_hub as hub
import tensorflow as tf
from matplotlib import pyplot as plt
import numpy as np
import cv2

model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

def load_image(img_path):
    img = tf.io.read_file(img_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

content_image = load_image('NEW PROFILE.jfif')
style_image = load_image('monet.jpeg')

content_image.shape

plt.imshow(np.squeeze(style_image))
plt.show()

stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]

plt.imshow(np.squeeze(stylized_image))
plt.show()

cv2.imwrite('generated_img.jpg', cv2.cvtColor(np.squeeze(stylized_image)*255, cv2.COLOR_BGR2RGB))













