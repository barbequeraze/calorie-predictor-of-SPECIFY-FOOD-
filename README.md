# Calorie Prediction from Macronutrients

Predicts the calorie content (kcal) of a food item from its protein, carbohydrate, fat, fiber and sugar content, using traditional machine learning. Final project for **241 – Machine Learning** (Instructor: Dr. Armida P. Salazar).

**Deployed app:** https://atmxcjmrgtxo2rv8zdwk6w.streamlit.app/

## Project Overview

This is a regression task. Three traditional algorithms were compared under identical conditions (same 80/20 train-test split, same preprocessing pipeline, same shuffled 5-fold cross-validation, same primary metric, random seed 42):

1. **Linear Regression**
2. **Decision Tree Regressor** (grid search, 135 combinations)
3. **Random Forest Regressor** (grid search, 54 combinations)

Linear Regression had the lowest cross-validation RMSE and was selected. It was evaluated once on the untouched test set.

| Model | CV RMSE (kcal) | CV MAE (kcal) | CV R² |
| --- | --- | --- | --- |
| Linear Regression | 30.04 ± 0.38 | 23.91 ± 0.41 | 0.9357 ± 0.0026 |
| Random Forest | 33.41 ± 0.85 | 26.33 ± 0.59 | 0.9205 ± 0.0037 |
| Decision Tree | 40.99 ± 0.69 | 32.40 ± 0.50 | 0.8804 ± 0.0038 |

**Final test result (Linear Regression):** RMSE 29.67 kcal, MAE 24.06 kcal, R² 0.9334.

## Dataset

- **Source:** Food Nutrition and Calories Dataset, Kaggle: https://www.kaggle.com/datasets/amineipad/food-nutrition-dataset-for-calorie-classification
- **License:** MIT
- **Records:** 5,000 food items (one row per food item)
- **Features:** `protein_g`, `carbs_g`, `fat_g`, `fiber_g`, `sugar_g` (grams)
- **Target:** `calories` (kcal)
- **Not used:** `calorie_class`, because it is derived from the target (leakage)
- The original file is in `data/original/` and is never modified. The cleaned file is in `data/processed/`.

## Folder Structure

```
calorie-predictor/
├── app/                 Streamlit application (app.py)
├── data/
│   ├── original/        Original dataset and source note
│   └── processed/       Cleaned dataset
├── notebooks/
│   ├── eda.ipynb
│   ├── linear_regression.ipynb
│   ├── decision_tree.ipynb
│   ├── random_forest.ipynb
│   └── final_model_evaluation.ipynb
├── src/                 Reusable preprocessing and modeling code
│   └── preprocess.py
├── models/              Saved best pipeline (preprocessing + model)
│   ├── best_pipeline.joblib
│   └── best_pipeline.json
├── documentation/       Technical documentation and screenshots
│   └── data_dictionary.md
├── paper/               Final paper (DOCX and PDF)
│   ├── Calorie Prediction Using Machine Learning and the Atwater Formula.docx
│   └── Calorie Prediction Using Machine Learning and the Atwater Formula.pdf
├── README.md
└── requirements.txt
```

## Installation

Requires Python 3.11. Run these commands in a terminal.

1. Clone the repository:

   ```bash
   git clone https://github.com/barbequeraze/the-boys_calorie-predictor-using-ml.git
   cd the-boys_calorie-predictor-using-ml
   ```

2. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the App Locally

From the repository root:

```bash
streamlit run app/app.py
```

The app opens in your browser (default http://localhost:8501).

## Reproduce the Results

Run the notebooks from the `notebooks/` folder in this order, each from top to bottom:

1. `eda.ipynb`: data quality checks, plots, and the processed dataset
2. `linear_regression.ipynb`, `decision_tree.ipynb`, `random_forest.ipynb`: cross-validation for each model (the test set is not used)
3. `final_model_evaluation.ipynb`: one-time test evaluation, residual analysis, and saving the pipeline to `models/`

All notebooks use `RANDOM_STATE = 42` and the same split, so results are reproducible.

## Using the App

Enter the nutrient values for one food item and the app returns the predicted calories (kcal) and the name of the model used (Linear Regression).

| Field | Unit | Allowed range |
| --- | --- | --- |
| Protein | g | 0 to 300 |
| Carbohydrates | g | 0 to 300 |
| Fat | g | 0 to 300 |
| Fiber | g | 0 to 300 |
| Sugar | g | 0 to 300 |

Input rules:
- Negative values are not accepted.
- At least one nutrient must be greater than 0.
- Blank or non-numeric entries revert to default values instead of crashing the app.

The output is a single estimate in kcal. Linear Regression does not provide class probabilities.

## Model Limitations

- Trained on one dataset of 5,000 records, and the data may be synthetic (for example, sugar and carbohydrates are uncorrelated, and every feature has a spike at zero). Results may differ on measured food-composition data.
- Uses five nutrients only. Portion size, preparation method, alcohol and water content are not considered.
- Typical error is about 24 kcal (MAE), roughly 5% of an average food item. It is not suitable for uses that need label-grade precision.
- Inputs far outside the training range (for example, carbohydrates above about 120 g) are extrapolations and may be less reliable.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `ModuleNotFoundError` | Activate your virtual environment and run `pip install -r requirements.txt` again. |
| `FileNotFoundError` for the model | Run `streamlit run app/app.py` from the repository root, and make sure the saved pipeline exists in `models/` (run `final_model_evaluation.ipynb` to create it). |
| Warning about scikit-learn version when loading the model | Install the exact versions in `requirements.txt`. |
| Notebook cannot find `calorie_dataset.csv` | Place it in `data/original/` (see the Dataset section for the download link). |
| Port already in use | Run `streamlit run app/app.py --server.port 8502`. |

## Authors

Millonte, Lord Cedrick M.\
Luna, Robi Troy\
Manalang, Wil Conrad\
Cadiz, Jefferson de

## Acknowledgments and References

Dataset: see the Kaggle link above (MIT License). Built with Python, pandas, scikit-learn and Streamlit. Full references are in the project paper (`paper/`).
