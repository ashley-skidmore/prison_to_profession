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


# ## Mapping Function

# In[ ]:


def map_column(
    df: pd.DataFrame,
    column: str,
    mapping_dict: Dict,
    new_column: Optional[str] = None
) -> pd.DataFrame:
    """
    Maps the values in a given column using a dictionary and adds the result
    to a new column or overwrites the original.

    Args:
        df: The DataFrame to modify.
        column: The name of the column to map.
        mapping_dict: A dictionary with keys as original values and values as mapped labels.
        new_column: If provided, mapped values will go into this new column.
                    If None, the original column will be overwritten.

    Returns:
        A DataFrame with the mapped column added or replaced.
    """
    mapped_values = df[column].map(mapping_dict).astype(str)

    if new_column:
        df[new_column] = mapped_values
    else:
        df[column] = mapped_values

    return df


# ## Null Handling Function

# In[ ]:


def clean_nulls(
    df: pd.DataFrame,
    strategy: str = "drop", #the default if strategy isn't chosen
    fill_value: Optional[Union[str, int, float]] = None,
    subset: Optional[list] = None
) -> pd.DataFrame:
    """
    Handles missing values in a DataFrame by dropping or filling.

    Args:
        df: The DataFrame to clean.
        strategy: "drop" to remove rows with nulls, "fill" to replace them.
        fill_value: The value to use when filling. Required if strategy is "fill".
        subset: Optional list of column names to limit the cleaning to.

    Returns:
        A cleaned DataFrame with nulls dropped or filled.
    """
    initial_shape = df.shape

    if strategy == "drop":
        df = df.dropna(subset=subset)
        print(f"Dropped rows with nulls in {subset or 'all columns'}")

    elif strategy == "fill":
        if fill_value is None:
            raise ValueError("fill_value must be provided when strategy is 'fill'")
        df = df.fillna(value=fill_value)
        print(f"Filled nulls in {subset or 'all columns'} with '{fill_value}'")

    else:
        raise ValueError("strategy must be either 'drop' or 'fill'")

    print(f"Shape before: {initial_shape} → after: {df.shape}")
    return df


# ## Normalizing Columns Function

# In[ ]:


def normalize_column_names(df: pd.DataFrame, inplace: bool = True) -> pd.DataFrame:
    """
    Converts all column names in a DataFrame to snake_case:
    lowercase, no spaces or special characters.

    Args:
        df: The DataFrame to normalize.
        inplace: If True, modifies the original DataFrame. If False, returns a modified copy.

    Returns:
        The DataFrame with normalized column names.
    """
    def to_snake(name: str) -> str:
        # Remove special characters, strip, replace spaces with underscores, lowercase
        name = re.sub(r"[^\w\s]", "", name)
        """remove punctuation
        \w = any letter, number or underscore
        \s = spaces and tabs
        [^] = NOT any of the bracket contents
        """
        name = re.sub(r"\s+", "_", name.strip())  # replace spaces with underscores
        return name.lower()

    new_columns = [to_snake(col) for col in df.columns] #applies to_snake to every column name

    if inplace:
        df.columns = new_columns
        return df
    else:
        df_copy = df.copy()
        df_copy.columns = new_columns
        return df_copy


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

