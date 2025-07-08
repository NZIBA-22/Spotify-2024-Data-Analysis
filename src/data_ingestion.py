# src/data_ingestion.py

import os
import sys
from pathlib import Path

# Adiciona o diretório raiz ao path para encontrar o 'src'
PROJECT_ROOT = Path(__file__).parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from src import config
from kaggle.api.kaggle_api_extended import KaggleApi

def set_proxy(proxy_url: str | None):
    """Sets proxy environment variables."""
    if proxy_url:
        print(f"Setting proxy for this session: {proxy_url}")
        os.environ['HTTP_PROXY'] = proxy_url
        os.environ['HTTPS_PROXY'] = proxy_url

def standardize_filename():
    """Finds and renames the downloaded CSV to the standard project filename."""
    download_path = config.RAW_DATA_DIR
    expected_file_path = config.RAW_DATA_FILE
    downloaded_csvs = list(download_path.glob('*.csv'))
    if not downloaded_csvs:
        print("Error: No CSV file found after download.")
        return
    actual_file_path = downloaded_csvs[0]
    if actual_file_path.resolve() != expected_file_path.resolve():
        print(f"Standardizing: Renaming '{actual_file_path.name}' to '{expected_file_path.name}'...")
        actual_file_path.rename(expected_file_path)
        print("Filename standardized.")

def download_data():
    """
    Main function to download and prepare the raw dataset using settings from config.
    """
    set_proxy(config.PROXY_URL)
    
    if config.RAW_DATA_FILE.exists():
        print(f"Raw data file already exists at '{config.RAW_DATA_FILE}'. Skipping download.")
        return

    print(f"Downloading dataset '{config.KAGGLE_DATASET_ID}'...")
    try:
        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files(config.KAGGLE_DATASET_ID, path=config.RAW_DATA_DIR, unzip=True, quiet=True)
        print("Download and extraction complete.")
        standardize_filename()
    except Exception as e:
        print(f"An error occurred during download: {e}")