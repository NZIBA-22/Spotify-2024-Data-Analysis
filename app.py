import pandas as pd
import numpy as np
from flask import Flask, render_template, request
from pathlib import Path
import sys
from src import config
from src.analysis import get_key_performance_indicators, get_top_n_tracks
from src.modeling import load_model

# Add project root to sys.path to import from 'src'
PROJECT_ROOT = Path(__file__).parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Initialize Flask App
app = Flask(__name__)

# Load cleaned data and production model at startup
try:
    df_clean = pd.read_csv(config.CLEANED_DATA_FILE)
    production_model = load_model()
    print("Cleaned data and model loaded successfully.")
except FileNotFoundError as e:
    print(f"ERROR: Required file not found. {e}")
    print("Please run the data pipeline and model training first.")
    df_clean = None
    production_model = None

# Define routes
@app.route('/')
def dashboard():
    """
    Render the main dashboard with key performance indicators and top tracks.

    Returns:
        str: Rendered HTML template with KPIs and top 10 tracks.
    """
    if df_clean is None:
        return "Error: Cleaned data file not found. Please run the data pipeline first.", 500

    kpis = get_key_performance_indicators(df_clean)
    top_tracks = get_top_n_tracks(df_clean, n=10)

    return render_template('index.html', kpis=kpis, top_tracks=top_tracks)

@app.route('/simulator')
def simulator():
    """
    Render the simulator page with a form to input track parameters.

    Returns:
        str: Rendered simulator page.
    """
    return render_template('simulator.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle form submission for prediction and render the simulator with results.

    Returns:
        str: Rendered simulator page with prediction result or error message.
    """
    if production_model is None:
        return "Error: Trained model not found. Please run the modeling pipeline first.", 500

    try:
        form_data = request.form.to_dict()
        input_data = pd.DataFrame([form_data])
        for col in input_data.columns:
            input_data[col] = pd.to_numeric(input_data[col], errors='coerce')

        input_data = input_data[config.MODEL_FEATURES]
        predicted_score = production_model.predict(input_data)[0]
        result = f"{predicted_score:.2f}"

    except Exception as e:
        print(f"Error during prediction: {e}")
        result = "An error occurred while processing the input data."

    return render_template('simulator.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
