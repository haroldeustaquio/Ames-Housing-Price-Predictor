# Docker

## Summary

Esta carpeta contiene los archivos necesarios para construir y ejecutar el entorno Dockerizado del proyecto Ames Housing Price Predictor.

**Content**
- [Architecture](#architecture)
- [Dockerfile](#dockerfile)
- [app/](#app)
    - [main.py](#mainpy)
    - [preprocessing_blocks.py](#preprocessing_blockspy)
    - [generate_pipeline.py](#generate_pipelinepy)
- [Use](#use)

---

## Architecture



---

## Dockerfile

**Purpose:**  
Define la imagen base y los pasos para construir el contenedor de la aplicación.

**Main steps:**  
- Especifica la imagen base (Python).
- Copia los archivos de la aplicación y dependencias.
- Instala las dependencias necesarias.
- Expone el puerto de la API.
- Define el comando de inicio del contenedor.

---

## app/

### main.py

**Purpose:**  
Implementa la salida de la API para el modelo de predicción de precios de viviendas, ejecutándose dentro del contenedor Docker.

**Main steps:**  
- Carga el modelo previamente entrenado y sus dependencias.
- Define los endpoints de la API (por ejemplo, `/predict`).
- Recibe solicitudes HTTP con datos de entrada para predicción.
- Procesa los datos recibidos y realiza la predicción usando el modelo.
- Devuelve la predicción en formato JSON como respuesta de la API.



---

### preprocessing_blocks.py

**Purpose:**  
Contiene bloques reutilizables de preprocesamiento para el pipeline, como codificadores categóricos (`CatBoostEncoderWrapper`), ingeniería de variables (`FeatureEngineering`) y selección de columnas (`ColumnSelector`).

**Main steps:**  
- Codificación de variables categóricas usando CatBoostEncoder.
- Creación de nuevas variables relevantes para el modelo.
- Selección de subconjuntos de columnas para el pipeline.




---

### generate_pipeline.py

**Purpose:**  
Script para generar y guardar el pipeline de procesamiento y/o el modelo entrenado que será utilizado por la API.

**Main steps:**  
- Carga los datos procesados necesarios para el entrenamiento.
- Define y entrena el pipeline de preprocesamiento y el modelo.
- Guarda el pipeline y/o modelo en el formato requerido para su posterior uso en producción dentro del contenedor Docker.

---

## Use

1. Generar el pipeline y/o modelo antes de construir la imagen:
   ```sh
   cd docker
   python -m app.generate_pipeline
   ```
   Esto crea los archivos necesarios (pipeline/modelo) que serán incluidos en la imagen Docker.

2. Construir la imagen Docker:
   ```sh
   docker build -t housing-price-predictor-api .
   ```

3. Ejecutar el contenedor:
   ```sh
   docker run -p 8080:8080 housing-price-predictor-api
   ```

4. Verificar la API:
   Accede a la siguiente URL para comprobar que la API responde correctamente:
   ```
   http://localhost:8080/
   ```

   Puedes usar Postman, curl o tu navegador.  
   La respuesta esperada debe ser:

   ```json
   {
       "message": "Hi harold!!"
   }
   ```

---


