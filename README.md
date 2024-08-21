# Colibrí Predictor

## Descripción del Proyecto

Esta aplicación predice entre dos clases de colibríes: el **Colibrí Inca ventrivioleta** y el **Colibrí picoespada**. Ambas especies se encuentran en Colombia. El modelo de clasificación utiliza aprendizaje automático para determinar a qué especie pertenece la imagen del colibrí.

## Modo de Uso

1. **Construir el Contenedor Docker**

   Asegúrate de tener Docker instalado en tu PC. Luego, construye la imagen Docker con el siguiente comando:

   ```bash
   docker build -t colibri-predictor .
2. **Ejecutar el Contenedor**

    Una vez que la imagen esté construida, ejecuta el contenedor en el puerto 5000 con el siguiente comando:

    ```bash
    docker build -t colibri-predictor .
   ```
## Interacción con la Aplicación

1. **Subir Imagen:**
   - Abre tu navegador web y dirígete a [http://localhost:5000](http://localhost:5000) o en [http://127.0.0.1:5000](http://127.0.0.1:5000).
   - Verás un formulario que te permitirá seleccionar una imagen de un colibrí. Haz clic en el botón "Seleccionar archivo" o "Elegir archivo" para elegir una imagen de tu dispositivo.
   - Después de seleccionar la imagen, haz clic en el botón "Clasificar" para cargar la imagen a la aplicación.
   - La aplicación procesará la imagen y mostrará la predicción en la pantalla. Verás el nombre de la especie predicha: **Colibrí Inca ventrivioleta** o **Colibrí picoespada**.

2. **Volver a Predecir:**
   - Si deseas realizar otra predicción, haz clic en el botón "Volver a predecir" que aparece en la interfaz después de la primera predicción.
   - Esto te permitirá cargar una nueva imagen y obtener una nueva predicción.
   - 
## Configuración de Archivos

- **Modelo:** El modelo preentrenado está en formato `.h5`. Este modelo se encuentra en un proyecto aparte que puedes consultar para seguir entrenando con más colibríes. Puedes encontrar más información y el enlace al proyecto aquí: [Enlace al proyecto](https://github.com/carfolacam98/TrainingModel).

- **Archivos del Proyecto:**
  - `main.py`: Archivo principal que implementa la aplicación Flask y define la interfaz de la aplicación.
  - `templates/`: Carpeta que contiene los archivos HTML para la interfaz de usuario. Aquí se encuentran las plantillas que se renderizan en el navegador.
  - `static/`: Carpeta que contiene archivos estáticos como imágenes, CSS y JavaScript que se utilizan en la aplicación.
  - `preprocess.py`: Archivo que se encarga del procesamiento de imágenes JPEG y la carga del modelo para la predicción.

## Requisitos

Para ejecutar la aplicación, necesitas tener Docker instalado en tu máquina. No se requieren dependencias adicionales para el uso básico de la aplicación.

- **Docker:** Asegúrate de tener Docker instalado. Puedes descargarlo e instalarlo desde [Docker](https://www.docker.com/products/docker-desktop).
