import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Define output paths for static assets
STATIC_PATH = Path(__file__).parent.parent / 'static'
PLOTS_PATH = STATIC_PATH / 'plots'


def load_and_prepare_data(data_path: Path) -> pd.DataFrame:
    """
    Loads the cleaned dataset from a given path.

    Args:
        data_path (Path): Path to the cleaned CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    
    Raises:
        FileNotFoundError: If the file does not exist at the specified path.
    """
    if not data_path.exists():
        raise FileNotFoundError(f"Cleaned data file not found at {data_path}")
    return pd.read_csv(data_path, encoding='utf-8')


def get_key_performance_indicators(df: pd.DataFrame) -> dict:
    """
    Calculates key performance indicators (KPIs) from the dataset.

    Args:
        df (pd.DataFrame): The cleaned dataset.

    Returns:
        dict: Dictionary containing KPIs such as total tracks, unique artists,
              average streams, and the most streamed artist.
    """
    kpis = {
        'total_tracks': len(df),
        'total_artists': df['artist'].nunique(),
        'average_streams': f"{df['spotify_streams'].mean():,.0f}".replace(',', '.'),
        'most_popular_artist': df.groupby('artist')['spotify_streams'].sum().idxmax()
    }
    return kpis


def get_top_n_tracks(df: pd.DataFrame, n: int = 10) -> list[dict]:
    """
    Retrieves the top N most streamed tracks.

    Args:
        df (pd.DataFrame): The cleaned dataset.
        n (int): Number of top tracks to retrieve. Default is 10.

    Returns:
        list[dict]: List of dictionaries containing track name, artist, and formatted stream count.
    """
    top_df = df.nlargest(n, 'spotify_streams')
    result_df = top_df[['track', 'artist', 'spotify_streams']].copy()
    result_df['spotify_streams'] = result_df['spotify_streams'].apply(lambda x: f"{x:,.0f}".replace(',', '.'))
    return result_df.to_dict(orient='records')


def create_streams_distribution_plot(df: pd.DataFrame) -> str:
    """
    Creates and saves a histogram of track stream counts (in millions).

    Args:
        df (pd.DataFrame): The cleaned dataset.

    Returns:
        str: Relative path to the saved plot image.
    """
    PLOTS_PATH.mkdir(parents=True, exist_ok=True)
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.histplot(df['spotify_streams'] / 1_000_000, bins=30, kde=True, ax=ax, color='#1DB954')

    ax.set_title('Distribution of Track Streams (in Millions)', fontsize=16, color='white')
    ax.set_xlabel('Streams (Millions)', fontsize=12, color='white')
    ax.set_ylabel('Track Count', fontsize=12, color='white')
    ax.grid(axis='y', linestyle='--', alpha=0.3)
    ax.tick_params(colors='white')
    fig.patch.set_facecolor('#121212')
    ax.set_facecolor('#1e1e1e')

    plot_filename = 'streams_distribution.png'
    save_path = PLOTS_PATH / plot_filename
    plt.savefig(save_path, bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()

    return f'plots/{plot_filename}'
