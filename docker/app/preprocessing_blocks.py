from category_encoders import CatBoostEncoder
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class CatBoostEncoderWrapper(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.encoder = None
        self.categorical_cols = []
        self.fitted = False
        self.target = 'saleprice'
        
    def fit(self, df: pd.DataFrame, y = None):
        # Detecta columnas categóricas automáticamente
        self.categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
        if not self.categorical_cols:
            raise ValueError("No se encontraron columnas categóricas en el DataFrame.")

        self.encoder = CatBoostEncoder(cols=self.categorical_cols, random_state=0)
        self.encoder.fit(df[self.categorical_cols], df[self.target])
        self.fitted = True
        return self

    def transform(self, df: pd.DataFrame):
        if not self.fitted:
            raise RuntimeError("Debes llamar primero a .fit() antes de usar .transform().")
        
        df_encoded = df.copy()
        df_encoded[self.categorical_cols] = self.encoder.transform(df[self.categorical_cols])
        
        return df_encoded

class FeatureEngineering(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, df, y=None):
        return self

    def transform(self, df):
        df = df.copy()
        # Crear nuevas columnas
        df["total_sqft"] = df["1st_flr_sf"] + df["2nd_flr_sf"] + df["total_bsmt_sf"]
        df["overall_score"] = df["overall_qual"] * df["overall_cond"]
        df["total_bathrooms"] = (df["full_bath"] + 0.5*df["half_bath"] + df["bsmt_full_bath"] + 0.5*df["bsmt_half_bath"])
        return df

class ColumnSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, df, y=None):
        return self
    
    def transform(self, df):
        return df[self.columns]
