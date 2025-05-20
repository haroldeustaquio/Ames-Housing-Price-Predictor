# Docker

## Summary

This folder contains the files needed to build and run the Dockerized environment for the Ames Housing Price Predictor project.

**Content**
- [Architecture](#architecture)
- [Dockerfile](#dockerfile)
- [app/](#app)
   - [main.py](#mainpy)
   - [preprocessing_blocks.py](#preprocessing_blockspy)
   - [generate_pipeline.py](#generate_pipelinepy)
- [Usage](#usage)

---

## Architecture

<p align="center">
  <img src="https://github.com/user-attachments/assets/6ee76023-2858-49fb-989c-c1bb1a90e465" alt="Architecture">
</p>

---

## Dockerfile

**Purpose:**  
Defines the base image and steps to build the application container.

**Main steps:**  
- Specifies the base image (Python).
- Copies application files and dependencies.
- Installs required dependencies.
- Exposes the API port.
- Sets the container startup command.

---

## app/

### main.py

**Purpose:**  
Implements the API output for the house price prediction model, running inside the Docker container.

**Main steps:**  
- Loads the pre-trained model and its dependencies.
- Defines API endpoints (e.g., `/predict`).
- Receives HTTP requests with input data for prediction.
- Processes received data and makes predictions using the model.
- Returns the prediction as a JSON response from the API.

---

### preprocessing_blocks.py

**Purpose:**  
Contains reusable preprocessing blocks for the pipeline, such as categorical encoders (`CatBoostEncoderWrapper`), feature engineering (`FeatureEngineering`), and column selection (`ColumnSelector`).

**Main steps:**  
- Encodes categorical variables using CatBoostEncoder.
- Creates new features relevant to the model.
- Selects column subsets for the pipeline.

---

### generate_pipeline.py

**Purpose:**  
Script to generate and save the processing pipeline and/or trained model to be used by the API.

**Main steps:**  
- Loads processed data needed for training.
- Defines and trains the preprocessing pipeline and model.
- Saves the pipeline and/or model in the required format for later use in production within the Docker container.

---

## Usage

1. Generate the pipeline and/or model before building the image:
   ```sh
   cd docker
   python -m app.generate_pipeline
   ```
   This creates the necessary files (pipeline/model) to be included in the Docker image.

2. Build the Docker image:
   ```sh
   docker build -t housing-price-predictor-api .
   ```

3. Run the container:
   ```sh
   docker run -p 8080:8080 housing-price-predictor-api
   ```

4. Verify the API:
   Access the following URL to check that the API is responding correctly:
   ```
   http://localhost:8080/
   ```

   You can use Postman, curl, or your browser.  
   The expected response should be:

   ```json
   {
      "message": "Hi harold!!"
   }
   ```

---
