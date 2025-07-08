"""
Central configuration file for the Spotify Analysis project.

This module defines constants, file paths, and model parameters
to ensure consistency and maintainability across the project.
All project-wide settings should be defined here.
"""

from pathlib import Path

# Project metadata
PROJECT_NAME = "Spotify_2024_Analysis"
AUTHOR = "Ludmyla Coimbra Muniz Cordeiro"

# Project root and main directories
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / 'data'
MODELS_DIR = PROJECT_ROOT / 'models'
REPORTS_DIR = PROJECT_ROOT / 'reports'
PLOTS_DIR = REPORTS_DIR / 'plots'

# Data subdirectories
RAW_DATA_DIR = DATA_DIR / 'raw'
PROCESSED_DATA_DIR = DATA_DIR / 'processed'

# File paths
RAW_DATA_FILE = RAW_DATA_DIR / 'most_streamed_spotify_songs_2024.csv'
CLEANED_DATA_FILE = PROCESSED_DATA_DIR / 'cleaned_spotify_data_2024.csv'
MODEL_FILE = MODELS_DIR / 'track_score_predictor.joblib'

# Ensure required directories exist
for path in [RAW_DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR, PLOTS_DIR]:
    path.mkdir(parents=True, exist_ok=True)

# Data ingestion settings
KAGGLE_DATASET_ID = 'nelgiriyewithana/most-streamed-spotify-songs-2024'

# Proxy configuration (if behind a corporate firewall)
# Example: "http://127.0.0.1:3128"
PROXY_URL = None

# Data cleaning parameters
GARBAGE_PATTERN = r'\ufffd|ý'
CRITICAL_COLS_FOR_CLEANING = ['track', 'artist']

# Modeling settings
TARGET_VARIABLE = 'track_score'

MODEL_FEATURES = [
    'spotify_streams',
    'spotify_playlist_count',
    'spotify_playlist_reach',
    'spotify_popularity',
    'youtube_views',
    'youtube_likes',
    'tiktok_posts',
    'tiktok_views',
    'shazam_counts',
    'airplay_spins',
    'days_since_release',
    'explicit_track'
]

XGB_PARAMS = {
    'objective': 'reg:squarederror',
    'n_estimators': 1000,
    'learning_rate': 0.05,
    'max_depth': 5,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'random_state': 42,
    'n_jobs': -1
}
