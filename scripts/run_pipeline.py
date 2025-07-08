"""
Main project pipeline script.

This script executes the entire data science workflow end-to-end:
1. Ingests raw data from Kaggle.
2. Cleans and processes the raw data.
3. Trains the predictive model and saves the artifact.
"""

import sys
from pathlib import Path

# Add project root to path to allow src imports
PROJECT_ROOT = Path(__file__).parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Import the main functions from our source modules
from src.data_ingestion import download_data
from src.data_processing import process_raw_data
from src.modeling import train_and_evaluate_model

def main():
    """Executes the full end-to-end pipeline."""
    print("=========================================")
    print("=== Starting Analysis of Spotify's Most Streamed Songs 2024 Data Pipeline ===")
    print("=========================================")

    print("\n[PIPELINE STEP 1/3] Ingesting Raw Data...")
    download_data()
    
    print("\n[PIPELINE STEP 2/3] Processing and Cleaning Data...")
    clean_df = process_raw_data()
    
    # Proceed only if the data processing was successful
    if clean_df is not None:
        print("\n[PIPELINE STEP 3/3] Training Predictive Model...")
        # Pass the cleaned DataFrame to the training function
        train_and_evaluate_model(clean_df) 
        
        print("\n=========================================")
        print("=== PIPELINE FINISHED SUCCESSFULLY ===")
        print("=========================================")
    else:
        print("\n=========================================")
        print("=== PIPELINE FAILED: Data processing error. ===")
        print("=========================================")


if __name__ == '__main__':
    main()