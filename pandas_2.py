import pandas as pd
import os

# Where our data lives..
CSV_PATH = os.path.join("C:/Users/jmcif/Downloads/ps/artwork_data.csv")

# Read 5 rows to see what's there
df = pd.read_csv(CSV_PATH, nrows = 5)

# Can also specify an index..
df = pd.read_csv(CSV_PATH, nrows = 5, 
                 index_col = "id")
# This means we can reuse an existing ID, instead of having 2 conflicting ones

# Limit column selection..
df = pd.read_csv(CSV_PATH, nrows = 5, 
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
