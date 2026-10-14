# Calorie Predictor

A machine learning project that predicts the calorie content of food items from their macronutrient.

## Project Overview

This project compares three traditional machine learning algorithms for a regression task:

1. **Linear Regression**
2. **Decision Tree Regressor**
3. **Random Forest Regressor**

All three models were trained and evaluated under identical experimental conditions: the same 80/20 train-test split, the same 5-fold cross-validation strategy, and the same preprocessing pipeline. This ensures a fair comparison.

Linear Regression achieved the lowest cross-validation RMSE (30.04 ± 0.38) and was selected as the final model. On the untouched test set, it achieved an RMSE of 29.67, MAE of 24.06, and R² of 0.9334. The learned coefficients approximated the Atwater energy conversion factors (~4 kcal/g for protein and carbohydrates, ~9 kcal/g for fat).
## Dataset

- **Source:**  https://www.kaggle.com/datasets/amineipad/food-nutrition-dataset-for-calorie-classification
- **Records:** 5,000 food items
- **Features:** protein_g, carbs_g, fat_g, fiber_g, sugar_g
- **Target:** calories

## Installation
In terminal follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/barbeque-raze/calorie-predictor-of-SPECIFY-FOOD-.git
   cd calorie-predictor-of-SPECIFY-FOOD-

2. Install dependecies:

   pip install -r requirements.txt

3. Runnin app locally:

   streamlit run app/app.py

   
