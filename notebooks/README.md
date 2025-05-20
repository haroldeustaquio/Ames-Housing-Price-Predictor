# Notebooks

## Summary

This directory contains the initial data exploration workflow for the Ames housing price prediction project.

**Content**
- [01_data_exploring.ipynb](#01_data_exploringipynb)
- [02_data_cleaning.ipynb](#02_data_cleaningipynb)
- [03_missing_values_imputation.ipynb](#03_missing_values_imputationipynb)
- [04_outlier_handling.ipynb](#04_outlier_handlingipynb)
- [05_feature_engineering.ipynb](#05_feature_engineeringipynb)
- [06_feature_selection.ipynb](#06_feature_selectionipynb)
- [07_model_selection.ipynb](#07_model_selectionipynb)
- [08_model_tuning.ipynb](#08_model_tuningipynb)

---

## 01_data_exploring.ipynb

**Purpose:**  
Explore and analyze the original dataset to identify relevant variables, review data quality, and define the first cleaning steps.

**Main steps:**  
- **Selection of relevant variables:**  
    Identify and justify the most important variables for the real estate business, classifying them according to their impact on house prices (`Neighborhood`, `Overall Qual`, `Gr Liv Area`, etc.), intermediate impact variables, and variables with no relevant impact.
- **Loading and visualizing data:**  
    Load the original dataset (`data.csv`) and display the first rows to understand the general structure.
- **Descriptive statistics:**  
    Calculate basic statistics (`df.describe()`) for all variables to detect outliers and unexpected ranges.
- **Review of columns and duplicates:**  
    List all columns and check for duplicate rows (ignoring identifiers).
- **Data types:**  
    Inspect the data types of each column to detect possible inconsistencies.
- **Conclusions and next steps:**  
    Document the next steps: remove irrelevant columns, standardize column names and types, and remove columns with a high percentage of nulls.

---

## 02_data_cleaning.ipynb

**Purpose:**  
Perform basic cleaning and preprocessing of the dataset to prepare the data for subsequent analysis and modeling stages.

**Main steps:**  
- **Removal of irrelevant columns:**  
    Remove columns that do not provide predictive value or have a high number of null values, based on business analysis and previous exploration.
- **Removal of columns with a high percentage of nulls:**  
    Identify and remove columns whose percentage of null values exceeds a defined threshold (e.g., 40%).
- **Standardization of column names:**  
    Normalize column names to `snake_case`, removing spaces and converting to lowercase for easier manipulation.
- **Review of duplicates:**  
    Check for duplicate rows in the dataset.
- **Inspection of data types:**  
    Review the data types of the columns and adjust them to appropriate formats (`float`, `Int64`, etc.) to ensure correct manipulation and further analysis.
- **Saving the cleaned dataset:**  
    The resulting dataset is saved in `parquet` format at `../data/processed/02_data_cleaned.parquet` for use in later stages.

---

## 03_missing_values_imputation.ipynb

**Purpose:**  
Impute missing values in the dataset using advanced and customized strategies according to the variable type.

**Main steps:**  
- **Analysis of null values:**  
    Perform a detailed analysis of numeric and categorical columns with null values, evaluating their quantity and distribution.
- **Recommendation of transformations:**  
    Recommend the appropriate transformation for each numeric variable before imputation, considering its distribution and presence of outliers.
- **Imputation of numeric variables:**  
    Select and apply the best imputation strategy for each numeric variable (`median`, `KNN`, etc.).
- **Imputation of categorical and integer variables:**  
    Use a `CatBoost` model to impute categorical and integer variables with high cardinality or complexity.
- **Saving the imputed dataset:**  
    The dataset with imputed missing values is saved at `../data/processed/03_data_imputed.parquet`.

---

## 04_outlier_handling.ipynb

**Purpose:**  
Detect and analyze outliers in the dataset to decide whether they should be removed or kept.

**Main steps:**  
- **Encoding categorical variables:**  
    Encode categorical variables to allow the application of numerical outlier detection methods.
- **Outlier detection with PCA:**  
    Use reconstruction by `PCA` to identify observations with high reconstruction error.
- **Outlier detection with Isolation Forest:**  
    Apply `Isolation Forest` to isolate anomalous observations.
- **Intersection and analysis of outliers:**  
    Identify outliers detected by both methods and analyze them.
- **Decision and saving:**  
    If the number of outliers is low or does not affect the analysis, decide not to remove them. The dataset is saved at `../data/processed/04_outlier_handling.parquet`.

---

## 05_feature_engineering.ipynb

**Purpose:**  
Create new relevant variables and remove redundant originals to improve the predictive power of the model.

**Main steps:**  
- **Creation of new variables:**  
    Generate variables such as `total_sqft`, `living_area_ratio`, `room_density`, `overall_score`, `exterior_score`, `house_age`, `years_since_remodel`, `total_bathrooms`, `has_fireplace`, `total_porch_sf`, `popular_neighborhood`, among others.
- **Removal of original columns:**  
    Remove original columns that have been replaced by the new variables.
- **Saving the enriched dataset:**  
    The enriched dataset is saved at `../data/processed/05_feature_engineering.parquet`.

---

## 06_feature_selection.ipynb

**Purpose:**  
Select the most relevant variables for the final model using different importance techniques.

**Main steps:**  
- **Encoding categorical variables:**  
    Encode categorical variables for analysis.
- **Importance ranking:**  
    Evaluate variable importance using correlation, mutual information, permutation, and SHAP.
- **Hyperparameter optimization:**  
    Perform hyperparameter search for regression models (`RandomForest`, `XGBoost`, `CatBoost`, `LightGBM`).
- **Selection of final variables:**  
    Select the most relevant variables and save the final dataset at `../data/processed/06_feature_selection.parquet`.

---

## 07_model_selection.ipynb

**Purpose:**  
Compare and select the best regression model for the problem.

**Main steps:**  
- **Model training:**  
    Train several models (`Bagging`, `Random Forest`, `Gradient Boosting`, `CatBoost`, `LightGBM`, `XGBoost`).
- **Evaluation with regression metrics:**  
    Evaluate the models using metrics such as MAE, MSE, RMSE, R², RMSLE, MAPE.
- **Visualization of results:**  
    Visualize importances, residuals, and learning curves.
- **Selection and saving of the best model:**  
    Select the best model and save it for later use.

---

## 08_model_tuning.ipynb

**Purpose:**  
Tune and optimize the best selected model to maximize its performance.

**Main steps:**  
- **Definition of the hyperparameter space:**  
    Define the search space for `CatBoost` hyperparameters.
- **Random hyperparameter search:**  
    Use `RandomizedSearchCV` to find the best configuration.
- **Evaluation and visualization:**  
    Evaluate the tuned model with metrics and visualizations of residuals, importances, and learning curves.
- **Saving the final model:**  
    The tuned model is saved at `../models/catboost_model_pro.cbm`.

---