import tensorflow as tf
import keras
import numpy as np
from EngSoft.settings import BASE_DIR

def initPrediction(img_path):
    
    model = tf.keras.models.load_model(f'{BASE_DIR}/prediction/model/meu_modelo.h5')
    
    classes = ['fracture', 'normal']

    img_height = 180
    img_width = 180

    print(img_path)
    
    img = keras.preprocessing.image.load_img(
        img_path, target_size=(img_height, img_width)
    )

    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    formatted_score = 100 * np.max(score)
    label = classes[np.argmax(score)]

    label_and_score = f"{label} with confidence: {formatted_score}%."

    return str(label_and_score)