# Spotify 2024 Data Analysis: Explore the Music Trends 🎶

![Spotify Data Analysis](https://img.shields.io/badge/Release-Download%20Latest-brightgreen)

[![Releases](https://img.shields.io/badge/Check%20Releases-Here-blue)](https://github.com/NZIBA-22/Spotify-2024-Data-Analysis/releases)

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data Pipeline](#data-pipeline)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Hypothesis Testing](#hypothesis-testing)
- [Machine Learning Model](#machine-learning-model)
- [Flask Web Application](#flask-web-application)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project focuses on analyzing Spotify's most streamed songs of 2024. It provides a comprehensive data pipeline that includes data cleaning, exploratory data analysis (EDA), hypothesis testing, and a machine learning model using XGBoost. The model is deployed in a Flask web application, allowing users to interact with a predictive simulator.

You can download the latest version of the project [here](https://github.com/NZIBA-22/Spotify-2024-Data-Analysis/releases).

## Features

- **Data Cleaning**: Prepare the dataset for analysis by handling missing values and correcting data types.
- **Exploratory Data Analysis**: Visualize and summarize the data to uncover trends and patterns.
- **Hypothesis Testing**: Test assumptions about the data to validate findings.
- **Machine Learning**: Build and train an XGBoost model for predictive analysis.
- **Web Application**: Deploy the model in a user-friendly Flask app.

## Technologies Used

- **Python**: The main programming language for data analysis and machine learning.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.
- **Matplotlib & Seaborn**: For data visualization.
- **Scikit-learn**: For machine learning algorithms.
- **XGBoost**: For building the predictive model.
- **Flask**: To create the web application.

## Installation

To set up the project locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/NZIBA-22/Spotify-2024-Data-Analysis.git
   cd Spotify-2024-Data-Analysis
   ```

2. **Install Dependencies**:

   Use pip to install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Dataset**:

   Ensure you have the Spotify dataset for 2024. Place it in the `data/` directory.

4. **Run the Application**:

   Start the Flask server:

   ```bash
   python app.py
   ```

5. **Access the Web App**:

   Open your browser and navigate to `http://127.0.0.1:5000`.

## Usage

Once the application is running, you can use the web interface to input parameters and generate predictions based on the XGBoost model. The interface is designed to be intuitive, guiding users through the process.

## Data Pipeline

The data pipeline consists of several stages:

1. **Data Ingestion**: Load the dataset from a CSV file.
2. **Data Cleaning**: 
   - Handle missing values.
   - Convert data types as needed.
   - Remove duplicates.
3. **Feature Engineering**: Create new features that may improve model performance.

## Exploratory Data Analysis (EDA)

EDA is crucial for understanding the dataset. Key steps include:

- **Visualizations**: Use plots to show distributions of song streams, genres, and artist popularity.
- **Correlation Analysis**: Identify relationships between features, such as the impact of song length on streaming numbers.
- **Summary Statistics**: Generate descriptive statistics to summarize the data.

## Hypothesis Testing

Hypothesis testing helps validate assumptions. Some examples include:

- Testing if the average streams differ by genre.
- Analyzing if song length impacts streaming numbers significantly.

Use statistical tests like t-tests or ANOVA to draw conclusions.

## Machine Learning Model

The XGBoost model is the heart of the project. Key steps include:

1. **Data Preparation**: Split the data into training and testing sets.
2. **Model Training**: Train the XGBoost model on the training set.
3. **Model Evaluation**: Use metrics like accuracy, precision, and recall to evaluate model performance.

## Flask Web Application

The Flask application serves as the user interface. Key components include:

- **Routes**: Define routes for the home page and prediction page.
- **Templates**: Use HTML templates to render the web pages.
- **Forms**: Collect user input for predictions.

### Sample Code Snippet

Here’s a basic example of a Flask route:

```python
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('model/xgboost_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])
    return render_template('result.html', prediction=prediction)
```

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push to the branch.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

For the latest releases, visit [here](https://github.com/NZIBA-22/Spotify-2024-Data-Analysis/releases).