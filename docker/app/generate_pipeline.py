from app.preprocessing_blocks import CatBoostEncoderWrapper, FeatureEngineering, ColumnSelector
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib

df = pd.read_parquet("app/../../data/processed/04_outlier_handling.parquet")
df = df[[
    '1st_flr_sf', '2nd_flr_sf', 'total_bsmt_sf', 'overall_qual', 'overall_cond', 
    'neighborhood', 'gr_liv_area','full_bath', 'half_bath', 'bsmt_full_bath', 
    'bsmt_half_bath', 'garage_cars', 'kitchen_qual','garage_area', 'saleprice'
    ]]

pipeline = Pipeline([
    ("catboost_imputer", CatBoostEncoderWrapper()),
    ("feature_engineering", FeatureEngineering()),
    ("catboost_wrapper", ColumnSelector([
        'total_bsmt_sf', 'overall_qual', 'neighborhood', 'gr_liv_area',
        'total_bathrooms', 'overall_score', 'garage_cars', 'kitchen_qual',
        'garage_area', 'saleprice'
    ])),
])

pipeline.fit(df)
joblib.dump(pipeline, "app/pipeline.pkl")
print("✅ pipeline.pkl generado correctamente")
