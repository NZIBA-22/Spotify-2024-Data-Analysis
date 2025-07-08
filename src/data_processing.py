"""
Module for all data ingestion, cleaning, and preparation tasks.

This script processes the raw data from Kaggle and transforms it into a clean,
analysis-ready DataFrame. All cleaning steps are encapsulated in a single function.
"""

import pandas as pd
import numpy as np
import ftfy
import chardet
import io
from pathlib import Path
from src import config  # Centralized configuration


def process_raw_data() -> pd.DataFrame | None:
    """
    Executes the full data processing pipeline:
    - Reads and decodes raw CSV
    - Cleans and standardizes data
    - Handles deduplication and type conversion
    - Saves cleaned dataset to disk

    Returns:
        pd.DataFrame | None: The cleaned dataset, or None if raw file is not found.
    """
    print("Starting Data Processing Pipeline...")

    raw_file_path = config.RAW_DATA_FILE
    processed_file_path = config.CLEANED_DATA_FILE

    if not raw_file_path.exists():
        print(f"Error: Raw data file not found at: {raw_file_path}")
        print("Please run the dataset download script before processing.")
        return None

    print(f"Reading raw data from: {raw_file_path}")
    with open(raw_file_path, 'rb') as raw_file:
        raw_data = raw_file.read()

    detected_encoding = chardet.detect(raw_data)['encoding']
    text_data = raw_data.decode(detected_encoding or 'latin-1', errors='replace')
    text_data = ftfy.fix_text(text_data)
    df = pd.read_csv(io.StringIO(text_data))
    print(f"Raw data successfully loaded with {len(df)} rows.")

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace(r'[()\[\]]', '', regex=True)
    print("Column names standardized.")

    # Remove rows with invalid characters in key fields
    initial_rows = len(df)
    df = df[~df['track'].str.contains(config.GARBAGE_PATTERN, na=False)]
    df = df[~df['artist'].str.contains(config.GARBAGE_PATTERN, na=False)]
    rows_removed = initial_rows - len(df)
    print(f"Removed {rows_removed} rows containing invalid characters.")

    # Remove rows with missing critical values and deduplicate
    df.dropna(subset=['track', 'artist'], inplace=True)
    df['track_normalized'] = df['track'].str.lower().str.strip()
    df['spotify_streams'] = pd.to_numeric(df['spotify_streams'].astype(str).str.replace(',', ''), errors='coerce')
    df.dropna(subset=['spotify_streams', 'track_normalized'], inplace=True)
    df['spotify_streams'] = df['spotify_streams'].astype('int64')
    df.sort_values('spotify_streams', ascending=False, inplace=True)
    
    dedup_initial = len(df)
    df.drop_duplicates(subset=['track_normalized'], keep='first', inplace=True)
    df.drop(columns=['track_normalized'], inplace=True)
    dedup_removed = dedup_initial - len(df)
    print(f"Removed {dedup_removed} duplicate tracks based on normalized names.")

    # Convert relevant columns to numeric
    numeric_cols = [
        'spotify_playlist_count', 'spotify_playlist_reach', 'youtube_views',
        'youtube_likes', 'tiktok_posts', 'tiktok_likes', 'tiktok_views',
        'youtube_playlist_reach', 'airplay_spins', 'siriusxm_spins',
        'deezer_playlist_reach', 'pandora_streams', 'pandora_track_stations',
        'soundcloud_streams', 'shazam_counts'
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')

    # Handle date parsing and missing values
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df.dropna(subset=['release_date'], inplace=True)
    numeric_fill_cols = df.select_dtypes(include=np.number).columns.tolist()
    df[numeric_fill_cols] = df[numeric_fill_cols].fillna(0)

    print("Final data type conversions and missing value handling completed.")

    # Save cleaned data
    processed_file_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(processed_file_path, index=False, encoding='utf-8')
    print(f"\nSaved {len(df)} cleaned records to: {processed_file_path}")
    print("Data Processing Pipeline Completed Successfully.")

    return df


if __name__ == '__main__':
    process_raw_data()
