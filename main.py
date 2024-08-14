import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Cargar el modelo
model = tf.keras.models.load_model('colibri_classifier_model.h5')

# Función para preprocesar la imagen
def preprocess_image(img_path, target_size):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Ruta a la imagen de prueba y tamaño objetivo del modelo
img_path = 'picoespada80.jpg'
target_size = (224, 224)  # Ajusta esto al tamaño de entrada de tu modelo

# Preparar la imagen
img_array = preprocess_image(img_path, target_size)


# Realizar la predicción
predictions = model.predict(img_array)
predicted_class_index = np.argmax(predictions, axis=1)[0]
class_labels = {0: 'Colibrí Inca ventrivioleta (Coeligena helianthea)', 1: 'Colibrí picoespada (Ensifera ensifera)'}
predicted_class_label = class_labels.get(predicted_class_index, 'Desconocida')
# Obtener la clase con la mayor probabilidad
probability = predictions[0][predicted_class_index]
print(f'Clase predicha: {predicted_class_label} y su probabilidad {probability*100}%')
