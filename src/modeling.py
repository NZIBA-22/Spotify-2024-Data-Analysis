import pandas as pd
import xgboost as xgb
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

from src import config
from src.visualization import plot_actual_vs_predicted


def train_and_evaluate_model(df: pd.DataFrame) -> xgb.XGBRegressor:
    """
    Trains, evaluates, and saves an XGBoost regression model.

    This function:
    - Performs final feature engineering
    - Prepares training/testing data
    - Trains the model with configured hyperparameters
    - Evaluates performance using R² and MAE
    - Saves the trained model to disk
    - Visualizes predictions

    Args:
        df (pd.DataFrame): Cleaned and preprocessed dataset.

    Returns:
        xgb.XGBRegressor: The trained XGBoost model.
    """
    print("Starting model training pipeline...")

    print("Performing final feature engineering...")
    df['release_date'] = pd.to_datetime(df['release_date'])
    df['days_since_release'] = (pd.to_datetime('2025-07-07') - df['release_date']).dt.days

    print("Preparing features and target variable...")
    X = df[config.MODEL_FEATURES].copy()
    y = df[config.TARGET_VARIABLE].copy()

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"Split data: {len(X_train)} for training, {len(X_test)} for testing.")

    print("Training XGBoost model...")
    model = xgb.XGBRegressor(**config.XGB_PARAMS)
    model.fit(X_train, y_train)
    print("Model training completed.")

    print("Evaluating model performance on test data...")
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"R-squared (R²): {r2:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")

    plot_actual_vs_predicted(y_test, y_pred, title="Model Performance: Actual vs. Predicted")

    print(f"Saving trained model to: {config.MODEL_FILE}")
    joblib.dump(model, config.MODEL_FILE)
    print("Model saved successfully.")

    print("Model training pipeline finished.")
    return model


def load_model(model_path: Path = config.MODEL_FILE) -> xgb.XGBRegressor:
    """
    Loads a trained XGBoost model from disk.

    Args:
        model_path (Path): Path to the saved model file.

    Returns:
        xgb.XGBRegressor: The loaded model.

    Raises:
        FileNotFoundError: If the model file does not exist.
    """
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found at: {model_path}")

    print(f"Loading model from {model_path}...")
    model = joblib.load(model_path)
    return model


if __name__ == '__main__':
    print("Running model training module as a standalone script...")

    if config.CLEANED_DATA_FILE.exists():
        df_clean = pd.read_csv(config.CLEANED_DATA_FILE)
        train_and_evaluate_model(df_clean)
    else:
        print(f"Error: Cleaned dataset not found at {config.CLEANED_DATA_FILE}")
        print("Please execute the data processing script before training.")
