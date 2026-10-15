from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import KFold, cross_validate, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

RANDOM_STATE = 42
TEST_SIZE = 0.20
N_SPLITS = 5

FEATURES = ["protein_g", "carbs_g", "fat_g", "fiber_g", "sugar_g"]
TARGET = "calories"  

SCORING = {
    "rmse": "neg_root_mean_squared_error",
    "mae": "neg_mean_absolute_error",
    "r2": "r2",
}

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "original" / "calorie_dataset.csv"
PROCESSED_PATH = ROOT / "data" / "processed" / "calorie_dataset_processed.csv"
MODEL_PATH = ROOT / "models" / "calorie_best_pipeline.joblib"

def load_data(path=DATA_PATH):
    """Read the original dataset from the given CSV path."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {path}. Place calorie_dataset.csv in data/original/."
        )
    return pd.read_csv(path)


def split_data(df, test_size=TEST_SIZE, random_state=RANDOM_STATE):
    """80/20 random split into train and test sets (same seed everywhere).

    The split is random and not stratified because the target is continuous and
    the records are not time-ordered. Keep the test set untouched until the final
    model has been chosen.
    """
    X = df[FEATURES]
    y = df[TARGET]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def build_preprocessor():
    """Standardize the five numeric features.

    Used inside a Pipeline, so the scaler is fitted only on training data
    (and only on the training part of each cross-validation fold).
    """
    return ColumnTransformer(transformers=[("num", StandardScaler(), FEATURES)])


def build_pipeline(model):
    """Combine the shared preprocessing step with any scikit-learn regressor."""
    return Pipeline([("pre", build_preprocessor()), ("model", model)])


def build_cv(n_splits=N_SPLITS, random_state=RANDOM_STATE):
    """Shuffled K-fold object. Reuse the same one for every model."""
    return KFold(n_splits=n_splits, shuffle=True, random_state=random_state)

def summarize_cv(model, name, X_train, y_train, cv=None, verbose=True):
    """5-fold CV on the TRAINING set only; returns mean and std of RMSE, MAE and R2."""
    cv = cv if cv is not None else build_cv()
    res = cross_validate(model, X_train, y_train, cv=cv, scoring=SCORING)
    rmse, mae, r2 = -res["test_rmse"], -res["test_mae"], res["test_r2"]
    if verbose:
        print(name)
        print(f"CV RMSE: {rmse.mean():.4f} +/- {rmse.std():.4f}")
        print(f"CV MAE : {mae.mean():.4f} +/- {mae.std():.4f}")
        print(f"CV R2  : {r2.mean():.4f} +/- {r2.std():.4f}")
    return {
        "model": name,
        "rmse_mean": rmse.mean(), "rmse_std": rmse.std(),
        "mae_mean": mae.mean(), "mae_std": mae.std(),
        "r2_mean": r2.mean(), "r2_std": r2.std(),
    }


if __name__ == "__main__":
    data = load_data()
    X_tr, X_te, y_tr, y_te = split_data(data)
    print("Train:", X_tr.shape, "| Test:", X_te.shape)
