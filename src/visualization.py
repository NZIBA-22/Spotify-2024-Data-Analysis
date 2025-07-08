"""
Module for generating standardized project visualizations.

This module contains reusable functions for creating plots like correlation
heatmaps, distribution plots, and other custom visualizations used throughout
the project's notebooks.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud
from pathlib import Path
from src import config 

def plot_correlation_heatmap(df: pd.DataFrame, cols: list, title: str, save_path: Path = None):
    """
    Generates, displays, and optionally saves a correlation heatmap.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        cols (list): A list of column names to include in the correlation matrix.
        title (str): The title for the plot.
        save_path (Path, optional): Path to save the figure. Defaults to None.
    """
    plt.figure(figsize=(12, 10))
    corr_matrix = df[cols].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='viridis', fmt='.2f')
    plt.title(title, fontsize=16)
    
    if save_path:
        save_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path, bbox_inches='tight')
        print(f"Plot saved to: {save_path}")
        
    plt.show()

def plot_top_n_bar_chart(data: pd.Series, title: str, xlabel: str, ylabel: str, color_palette: str = 'plasma'):
    """
    Generates and displays a horizontal bar chart for Top N items.

    Args:
        data (pd.Series): A pandas Series with index as labels and values as data.
        title (str): The title for the plot.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.
        color_palette (str, optional): Seaborn color palette. Defaults to 'plasma'.
    """
    plt.figure(figsize=(12, 8))
    sns.barplot(x=data.values, y=data.index, palette=color_palette)
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_actual_vs_predicted(y_true: pd.Series, y_pred: np.ndarray, title: str):
    """
    Creates a scatter plot of actual vs. predicted values for regression evaluation.

    Args:
        y_true (pd.Series): The true target values.
        y_pred (np.ndarray): The predicted values from the model.
        title (str): The title for the plot.
    """
    plt.figure(figsize=(10, 10))
    sns.scatterplot(x=y_true, y=y_pred, alpha=0.6)
    # Add a diagonal line for reference (perfect prediction)
    perfect_line = [min(y_true.min(), y_pred.min()), max(y_true.max(), y_pred.max())]
    plt.plot(perfect_line, perfect_line, '--', color='red', linewidth=2, label='Perfect Prediction')
    plt.title(title, fontsize=16)
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.legend()
    plt.grid(True)
    plt.show()