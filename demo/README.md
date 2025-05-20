# Demo 🏡

## Summary

For demonstration purposes, due to the large number of columns in the original dataset, only the main variables were selected to simplify the workflow. New models were trained exclusively for this demo using these selected features, achieving results similar to the full-feature models.

**Contents**
- [Main Steps](#main-steps)
- [Model Results](#model-results-test-set)
---

## Main Steps

- **Loading processed data:**  📂
    The cleaned and processed dataset is loaded from `../data/processed/04_outlier_handling.parquet`.

- **Preprocessing pipeline:**  🛠️
    Includes selection of relevant columns, categorical encoding with CatBoostEncoder, and creation of new features (`total_sqft`, `overall_score`, `total_bathrooms`).

- **Data splitting:**  ✂️
    Separation into training and test sets.

- **Model training and comparison:**  🤖📊
    Training of several models (`Bagging`, `Random Forest`, `Gradient Boosting`, `CatBoost`, `LightGBM`, `XGBoost`) and comparison using regression metrics (MAE, MSE, RMSE, R², etc.).

- **Results visualization:**  📈
    Plots of feature importances, residuals, scatter plots, and learning curves.

- **Best model selection and saving:**  🏆💾
    Selection of the best-performing model and saving it in CatBoost format.

- **Hyperparameter tuning:**  🎯
    Randomized hyperparameter search for `CatBoost` and evaluation of the tuned model.

---

## Model Results (test set) 📋

**Without hyperparameter tuning:**

| Model               | MAE         | MSE           | RMSE        | R²       | RMSLE    | MAPE    |
|---------------------|-------------|---------------|-------------|----------|----------|---------|
| Bagging Regressor   | 18,104.71   | 6.71e+08      | 25,902.84   | 0.9033   | 0.1479   | 0.1086  |
| Random Forest       | 17,538.71   | 6.69e+08      | 25,870.07   | 0.9035   | 0.1475   | 0.1061  |
| Gradient Boosting   | 17,431.24   | 6.11e+08      | 24,721.84   | 0.9119   | 0.1382   | 0.1029  |
| CatBoost            | 18,244.50   | 7.51e+08      | 27,410.27   | 0.8917   | 0.1393   | 0.1040  |
| LightGBM            | 17,474.67   | 6.73e+08      | 25,947.88   | 0.9029   | 0.1415   | 0.1024  |
| XGBoost             | 18,809.74   | 7.82e+08      | 27,968.33   | 0.8872   | 0.1484   | 0.1092  |

**With CatBoost hyperparameter tuning:**

| Model    | MAE         | MSE           | RMSE        | R²       | RMSLE    | MAPE    |
|----------|-------------|---------------|-------------|----------|----------|---------|
| CatBoost | 17,337.86   | 6.20e+08      | 24,908.48   | 0.9105   | 0.1377   | 0.1017  |

These results confirm that the simplified pipeline retains most of the predictive power, and that tuning further improves CatBoost's performance. 🚀