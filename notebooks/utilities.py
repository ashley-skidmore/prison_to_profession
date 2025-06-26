#!/usr/bin/env python
# coding: utf-8

# # Reusable Functions

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import os
from typing import Dict, Optional, Union  
"""
Mapping function: Dict for mapping dictionaries, Optional for allowing None values
Null handling function: Union means the value can be any of the listed types, like str, int, or float
"""
import re
"""
Normalize columns function: regular expressions to convert column names
"""


# ## Exploratory Data Analysis Function

# In[ ]:


import pandas as pd

def basic_eda(df: pd.DataFrame, show_head: bool = True, show_tail: bool = True, show_info: bool = True) -> None:
    """
    Prints a quick summary of a DataFrame, including shape, column names, data types,
    missing values, and optional previews of the data.

    Args:
        df: The pandas DataFrame to summarize.
        show_head: Whether to display df.head(). Default is True.
        show_tail: Whether to display df.tail(). Default is True.
        show_info: Whether to display df.info(). Default is True.

    Returns:
        None. Outputs printed summaries to the console.
    """

    print("DataFrame Shape:", df.shape)
    print("\n Column Names:")
    print(df.columns.tolist())

    print("\n Data Types:")
    print(df.dtypes)

    if show_info:
        print("\n DataFrame Info:")
        df.info()

    print("\n Null Values (%):")
    nulls = df.isnull().mean() * 100 #mean will give the decimal of total missing values and  * 100 will turn that into a percentage
    print(nulls[nulls > 0].round(2).sort_values(ascending=False)) #only displays columns with nulls, round the percen to 2 decimal places, and sorts high to low

    if show_head:
        print("\n Preview (Head):")
        print(df.head())

    if show_tail:
        print("\n Preview (Tail):")
        print(df.tail())


# ## Plot Style Function

# In[ ]:


def styled_plot(title: str, xlabel: str, ylabel: str, fontsize: int = 12) -> str:
    """
    Applies a consistent, custom-branded style to a matplotlib plot.

    Colors used:
      • Plot elements: Gold/Orange (#E7A614)
      • Title & Axis labels: KCTCS Blue (#00467F)
      • Ticks & Spines: Deep Navy (#011D41)

    Args:
        title (str): Plot title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
        fontsize (int, optional): Base font size for text elements. Default is 12.

    Returns:
        str: Hex color code for use in plotting data elements (e.g., bars, lines).
    """
    plot_color = "#E7A614"    # Orange-gold for bars/lines/etc.
    label_color = "#00467F"   # KCTCS Blue for text
    spine_color = "#011D41"   # Deep navy for spines and ticks

    plt.title(title, fontsize=fontsize + 2, color=label_color)
    plt.xlabel(xlabel, fontsize=fontsize, color=label_color)
    plt.ylabel(ylabel, fontsize=fontsize, color=label_color)
    plt.tick_params(axis='both', labelsize=fontsize - 1, colors=spine_color)

    ax = plt.gca()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(spine_color)
    ax.spines["bottom"].set_color(spine_color)
    plt.grid(False)

    return plot_color #variable to use for a consistent color when making plots


# ## Image File Function
# 
# ### **IMPORTANT**:
# - This function works on the most recently created plot.
# - Save plot before showing it to avoid saving a blank image.

# In[ ]:


def save_plot(filename: str, folder: str = "plots", dpi: int = 300) -> None:
    """
    Saves the current matplotlib figure as an image file.

    Args:
        filename (str): Name of the file (e.g., 'education_bar.png').
        folder (str, optional): Folder to save the file in. Defaults to 'plots'.
        dpi (int, optional): Resolution of the saved image. Defaults to 300.

    Returns:
        None
    """
    # Create the folder if it doesn't exist
    os.makedirs(folder, exist_ok=True)

    # Build full file path
    filepath = os.path.join(folder, filename)

    # Save the figure
    plt.savefig(filepath, dpi=dpi, bbox_inches='tight')
    print(f"Plot saved to: {filepath}")

