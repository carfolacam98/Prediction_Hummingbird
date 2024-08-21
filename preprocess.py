from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

model = load_model('colibri_classifier_model.h5')

class_labels = {
    0: 'Colibrí Inca ventrivioleta (Coeligena helianthea)',
    1: 'Colibrí picoespada (Ensifera ensifera)'
}

def predict_with_labels(img_path):

    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)


    preds = model.predict(x)


    predicted_class_index = np.argmax(preds, axis=1)[0]


    predicted_class_label = class_labels.get(predicted_class_index, 'Desconocida')
    probability = preds[0][predicted_class_index]
    return (predicted_class_label, probability)
