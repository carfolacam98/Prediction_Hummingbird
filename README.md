# Colibrí Predictor

## Descripción del Proyecto

Esta aplicación predice entre dos clases de colibríes: el **Colibrí Inca ventrivioleta** y el **Colibrí picoespada**. Ambas especies se encuentran en Colombia. El modelo de clasificación utiliza aprendizaje automático para determinar a qué especie pertenece la imagen del colibrí.

## Requisitos

Para ejecutar la aplicación, necesitas tener Docker instalado en tu máquina. No se requieren dependencias adicionales para el uso básico de la aplicación.

- **Docker:** Asegúrate de tener Docker instalado. Puedes descargarlo e instalarlo desde [Docker](https://www.docker.com/products/docker-desktop).

## Modo de Uso

 ### Construir el Contenedor Docker
1. **Localmente**

   Si cumples los requisitos puedes situarte en la raiz del proyecto y construye la imagen Docker con el siguiente comando:

   ```bash
   docker build -t colibri-predictor .
   ```
2. **Ejecutar el Contenedor**

    Una vez que la imagen esté construida, ejecuta el contenedor en el puerto 5000 con el siguiente comando:

    ```bash
    docker run -d -p 5000:5000 --name nombre-del-contenedor colibri-predictor
   ```
### Usar la Imagen Docker desde Docker Hub

Si no deseas construir la imagen localmente, puedes usar la imagen preconstruida disponible en Docker Hub. Sigue los siguientes pasos:

1. **Descargar la Imagen desde Docker Hub:**

   ```bash
   docker pull lauracamuao/colibri-predictor:latest

## Interacción con la Aplicación

1. **Subir Imagen:**
   - Abre tu navegador web y dirígete a [http://localhost:5000](http://localhost:5000) o en [http://127.0.0.1:5000](http://127.0.0.1:5000).
   - Verás un formulario que te permitirá seleccionar una imagen de un colibrí. Haz clic en el botón "Seleccionar archivo" o "Elegir archivo" para elegir una imagen de tu dispositivo.
   - Después de seleccionar la imagen, haz clic en el botón "Clasificar" para cargar la imagen a la aplicación.
   - La aplicación procesará la imagen y mostrará la predicción en la pantalla. Verás el nombre de la especie predicha: **Colibrí Inca ventrivioleta** o **Colibrí picoespada**.

2. **Volver a Predecir:**
   - Si deseas realizar otra predicción, haz clic en el botón "Volver a predecir" que aparece en la interfaz después de la primera predicción.
   - Esto te permitirá cargar una nueva imagen y obtener una nueva predicción.
   
## Configuración de Archivos

- **Modelo:** El modelo preentrenado está en formato `.h5`. Este modelo se encuentra en un proyecto aparte que puedes consultar para seguir entrenando con más colibríes. Puedes encontrar más información y el enlace al proyecto aquí: [Enlace al proyecto](https://github.com/carfolacam98/TrainingModel).
- **Imágenes Sugeridas:** Para entrenar y probar el modelo, puedes usar las imágenes disponibles en el siguiente enlace de Google Drive. Estas imágenes son adecuadas tanto para el entrenamiento del modelo como para realizar predicciones:
  - [Imágenes sugeridas](https://drive.google.com/drive/folders/1ulyyqQgHQG-ghzhqOV2JXsf55GbEr02n)
- **Archivos del Proyecto:**
  - `main.py`: Archivo principal que implementa la aplicación Flask y define la interfaz de la aplicación.
  - `templates/`: Carpeta que contiene los archivos HTML para la interfaz de usuario. Aquí se encuentran las plantillas que se renderizan en el navegador.
  - `static/`: Carpeta que contiene archivos estáticos como imágenes, CSS y JavaScript que se utilizan en la aplicación.
  - `preprocess.py`: Archivo que se encarga del procesamiento de imágenes JPEG ò PNG y la carga del modelo para la predicción.

## Colaboradoras

Este proyecto fue desarrollado por:

- **Angy Patarroyo**
- **Laura Cárdenas**

