import keras
import os
import keras
# import skimage
from PIL import Image
from keras.applications import inception_v3 as inc_net
from keras.preprocessing import image
from keras.applications.imagenet_utils import decode_predictions
# from skimage.io import imread
# from skimage.segmentation import mark_boundaries
import matplotlib.pyplot as plt
import numpy as np
model = keras.models.load_model('keras_wines_sparklings_model.h5')

labels_index = { 0 : "Open", 1 : "Close" }

def transform_img_fn(img):
    out = []
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = inc_net.preprocess_input(x)
    out.append(x)
    return np.vstack(out)

# Load image
wine_image = transform_img_fn(Image.open('wine.png'))

print(np.shape(wine_image))
# Show prediction

wine_image=wine_image.reshape(113, 270, 3)
preds = model.predict(wine_image)
print("Prediction: " + labels_index[int(preds[0][0])])