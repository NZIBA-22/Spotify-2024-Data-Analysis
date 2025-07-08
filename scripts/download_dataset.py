import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.append(str(PROJECT_ROOT))

from src.data_ingestion import download_data

if __name__ == '__main__':
    print("--- Running Data Ingestion Script ---")
    download_data()
    print("--- Data Ingestion Finished ---")