# Project Goal

A machine learning project that predicts the calorie content of food items based on their macronutrient profile.

## Project Overview

This project compares three traditional machine learning algorithms for a regression task:

1. **Linear Regression**
2. **Decision Tree Regressor**
3. **Random Forest Regressor**

The models were trained and evaluated under identical experimental conditions (same 80/20 train-test split, same 5-fold cross-validation strategy, and same preprocessing pipeline) to ensure a fair comparison. Linear Regression achieved the lowest cross-validation error and was selected as the final model.

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

   
