# Grouping

import pandas as pd
import numpy as np
import os

# Load the data
CSV_PATH = os.path.join("C:/Users/jmcif/Downloads/ps/artwork_data.csv")

df = pd.read_csv(CSV_PATH, nrows = 50, 
                 index_col = "id", 
                 usecols = ['id', 'artist'])

# All columns that we need
COLS_TO_USE = ['id', 'artist',
               'title', 'medium', 'year',
               'acquisitionYear', 'height',
               'width', 'units']

# Proper data loading
df = pd.read_csv(CSV_PATH, 
                 usecols=COLS_TO_USE, 
                 index_col='id')

small_df = df.iloc[49980:50019, :].copy()

# Group the small dataframe by artist
grouped = small_df.groupby('artist')

# Python stores this as an internal type called DataFrameGroupBy
type(grouped)

for name, group_df in grouped:
    print(name)
    print(group_df)
    break

# To find out what was an artist's first painting, we can search for the minimum date (lowest/earliest)
for name, group_df in small_df.groupby('artist'):
    min_year = group_df['acquisitionYear'].min()
    print("{}: {}".format(name, min_year))
    
# Below is a function which fills in values that aren't given, with the most common value relating to it

def fill_values(series):
    values_counted = series.value_counts()
    # if there are no values whatsoever, we cannot infer a most frequent value
    if values_counted.empty:
        return series
    most_frequent = values_counted.index[0]
    new_medium = series.fillna(most_frequent)
    return new_medium

def transform_df(source_df):
    # create an array called group_dfs
    group_dfs = []
    for name, group_df in source_df.groupby('artist'):
        filled_df = group_df.copy()
        filled_df.loc[:, 'medium'] = fill_values(group_df['medium'])
        group_dfs.append(filled_df)
    
    new_df = pd.concat(group_dfs)
    return new_df
    
filled_df = transform_df(small_df)
filled_df

# Built in-functions: transformation
grouped_mediums = small_df.groupby('artist')['medium']
small_df.loc[:, 'medium'] = grouped_mediums.transform(fill_values)

# Aggregation
grouped_acq_year = df.groupby('artist')['acquisitionYear']
min_acquisition_years = grouped_acq_year.agg(np.min)

# Even more efficient way
min_acquisition_years = grouped_acq_year.min()

grouped_titles = df.groupby('title')
condition = lambda x: len(x.index) > 1
filtered_df = grouped_titles.filter(condition)

# Demo..
df.groupby('artist').agg(np.min)

# Can also avoid NumPy, but it does have added benefits
df.groupby('artist').min()

# Filtering
grouped_titles = df.groupby('title')
title_counts = grouped_titles.size().sort_values(ascending = False)

condition = lambda x: len(x.index) > 1
dup_titles_df = grouped_titles.filter(condition)

dup_titles_df.sort_values('title', inplace = True)
