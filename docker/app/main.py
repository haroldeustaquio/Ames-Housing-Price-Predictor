from fastapi import FastAPI
from pydantic import BaseModel
from catboost import CatBoostRegressor, Pool
from app.preprocessing_blocks import (CatBoostEncoderWrapper, FeatureEngineering, ColumnSelector)
import joblib
import pandas as pd


app = FastAPI()

# Cargar modelo entrenado
pipeline = joblib.load("app/pipeline.pkl")
catboost_model = CatBoostRegressor()
catboost_model_pro = CatBoostRegressor()

# Cargar el modelo CatBoost
catboost_model.load_model('app/catboost_model_demo.cbm')
catboost_model_pro.load_model('app/catboost_model_demo_pro.cbm')

# Nombres de las columnas usados durante el entrenamiento
COLUMN_NAMES = [
    '1st_flr_sf', '2nd_flr_sf', 'total_bsmt_sf', 'overall_qual', 'overall_cond', 
    'neighborhood', 'gr_liv_area','full_bath', 'half_bath', 'bsmt_full_bath', 
    'bsmt_half_bath', 'garage_cars', 'kitchen_qual','garage_area'
    ]

# Modelo de entrada
class InputData(BaseModel):
    features: list

# Endpoint raíz
@app.get("/")
def root():
    return {"message": "Hi harold!!"}

@app.post("/predict")
def predict_explained(data: InputData):
    df = pd.DataFrame([data.features], columns=COLUMN_NAMES)
    df_transformed = pipeline.transform(df)
    
    # Convert the DataFrame to a Pool object
    input_pool = Pool(data=df_transformed)
    
    # Predict with the CatBoost model
    prediction = catboost_model.predict(input_pool)[0]
    prediction_pro = catboost_model_pro.predict(input_pool)[0]
    
    # Add bias to the prediction
    rmse = catboost_model.get_best_score()['learn']['RMSE']
    rmse_pro = catboost_model_pro.get_best_score()['learn']['RMSE']
    
    return {
        "prediction": [prediction, prediction - rmse, prediction + rmse],
        "prediction_pro": [prediction_pro, prediction_pro- rmse_pro, prediction_pro + rmse_pro],
    }