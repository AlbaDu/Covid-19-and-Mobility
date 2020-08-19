#Import the required libraries
import pandas as pd
from pandas import Grouper 
import numpy as np
#Import plotting modules
import seaborn as sns
sns.set()
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker

def file_to_df(file_):
    """
    ---What it does---
        + Generates a dataframe from a files: ".csv", ".xlsx" or ".xls".
    ---What it needs---
        + file: dataframe with columns.

    IMPORTANT! the files need to be stored in the path specified by the function.    
    ---What it returns---
        + new_df: dataframe containing the data from the file.
    """
    path = "C:\\Users\\34609\\Documents\\Repos Git\\Data\\"
    
    if file_.endswith("csv"):
        name = str(path + file_)
        new_df = pd.read_csv(name)
        return new_df
    elif file_.endswith("xlsx") or file_.endswith("xls"): 
        name = str(path + file_)
        new_df = pd.read_excel(name)
        return new_df

def country_df_generator(df, condition_1, condition_2):
    """
    ---What it does---
        + Generates a dataframe by country and date.
    ---What it needs---
        + df: dataframe with columns.
        + condition_1: name of the country.
        + condition_2: starting date.
    ---What it returns---
        + country_df
    """
    new_df = df[df["country"] == condition_1]
    new_df.drop(["country"], axis = 1, inplace = True)
    new_df.drop(new_df[new_df["date"] < condition_2].index, inplace = True)
    new_df.reset_index(drop = True, inplace = True)
    return new_df 

def df_weekly_generation(df):
    """
    ---What it does---
        + Generates a dataframe by country and date.
    ---What it needs---
        + big_df: dataframe with columns.
        + condition_1: name of the country.
        + condition_2: starting date.
    ---What it returns---
        + country_df
    """
    new_df = df.groupby(Grouper(key = "date", freq = '7D')).mean()
    new_df["week"] = range(0, len(new_df))
    new_df.set_index("week", inplace = True)
    return new_df

def category_df_generator (countries, dataframes, category):
    """
    ---What it does---
        + Generates a dataframe object combining different dataframes using a location as filter.
    ---What it needs---
        + countries: A list of country names
        + dataframes: A list of dataframes
        + category: The filter for dataframes. MUST be one of the df's columns contained in dataframes
    
    IMPORTANT! countries and dataframes MUST be ordered in the same way (e g. item#0 of countries must correspond with item#0 of dataframes)
    ---What it returns---
        + a new_df
    """
    new_df = pd.DataFrame(columns = countries)
    for e in range(new_df.shape[1]):
        new_df.iloc[:,e] = dataframes[e][category]  
    return new_df

def line_plot(df, title):
    """
    ---What it does---
    + Generates a line_plot.
    ---What it needs---
    + df: dataframe with a column as index, X, and other columns as variables.
    + title: plot's title.
    """
    sns.lineplot(data = df, palette = "tab10", linewidth = 2.5).set_title(title.upper());