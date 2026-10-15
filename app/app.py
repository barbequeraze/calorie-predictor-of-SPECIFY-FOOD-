import os
import json
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Calorie Predictor",
    page_icon="",
    layout="centered",
)

MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "models", "best_pipeline.json"
)

@st.cache_resource
def load_params(path):
    with open(path, "r") as f:
        return json.load(f)

try:
    params = load_params(MODEL_PATH)
except Exception as e:
    st.error(f"Could not load model parameters from: {MODEL_PATH}")
    st.exception(e)
    st.stop()

def predict(features_dict):
    x = np.array([features_dict[f] for f in params["features"]])
    x_scaled = (x - np.array(params["scaler_mean"])) / np.array(params["scaler_scale"])
    coef = np.array(params["coef"])
    return float(np.dot(x_scaled, coef) + params["intercept"])
st.title("Calorie Predictor")
st.markdown(
    "Predict the **calories** of a food item based on its macronutrient profile.\n\n"
    "**Model:** Linear Regression (selected via 5-fold cross-validation)."
)

with st.form("prediction_form"):
    st.subheader("Enter the macronutrient values")

    protein = st.number_input("Protein (g)",       min_value=0.0, max_value=200.0, value=25.0, step=0.1)
    carbs   = st.number_input("Carbohydrates (g)", min_value=0.0, max_value=300.0, value=50.0, step=0.1)
    fat     = st.number_input("Fat (g)",           min_value=0.0, max_value=200.0, value=20.0, step=0.1)
    fiber   = st.number_input("Fiber (g)",         min_value=0.0, max_value=100.0, value=8.0,  step=0.1)
    sugar   = st.number_input("Sugar (g)",         min_value=0.0, max_value=200.0, value=15.0, step=0.1)

    submitted = st.form_submit_button("Predict calories")

if submitted:
    if protein == 0 and carbs == 0 and fat == 0 and fiber == 0 and sugar == 0:
        st.warning("Please enter at least one non-zero macronutrient value.")
    else:
        try:
            pred = predict({
                "protein_g": protein,
                "carbs_g":   carbs,
                "fat_g":     fat,
                "fiber_g":   fiber,
                "sugar_g":   sugar,
            })
            st.success(f"### Predicted calories: {pred:.1f} kcal")
            st.caption(
                "Estimated using a Linear Regression model trained on 5,000 food items. "
                "This is not a substitute for professional nutritional advice, and the prediction should be used as a general guideline only."
            )
        except Exception as e:
            st.error("Prediction failed. Please check your inputs.")
            st.exception(e)

st.markdown("---")
st.markdown(
    """
    Goal: Predict the calorie content of a food item based on its macronutrient profile.

    Three traditional regression algorithms were compared under identical
    experimental conditions: Linear Regression, Decision Tree, and Random Forest.
    Linear Regression achieved the lowest cross-validation RMSE and was selected
    as the final model.

    Input features and units
    - `protein_g` — protein in grams
    - `carbs_g` — carbohydrates in grams
    - `fat_g` — fat in grams
    - `fiber_g` — fiber in grams
    - `sugar_g` — sugar in grams

    Output
    - Predicted calorie content in kcal per serving.
    """
)
