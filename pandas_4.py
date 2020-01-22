import pandas as pd
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

df

df.artist
artists = df['artists]

# To iron out how many unique values (in this case artists there are), use the .unique function
pd.unique(artists)

# To return how many there are, use the len() function 
len(pd.unique(artists))

# We can also apply filtering on data frames e.g.
s = df['artist'] == 'Bacon, Francis'
s.value_counts()

# Aside: alternative way to do it
artist_counts = df['artist'].value_counts()
artist_counts['Bacon, Francis']

# Below shows how to select by label (loc) - a reliable appraoch, the basic syntax is as follows

# df.loc[row_indexer, column_indexer]
# e.g.
df.loc[1035, 'artist']
# This means we want to select the 'artist' of the record_no 1035 (labels)

# Running the below code effectively produces a data frame with all records pertaining to Francis Bacon
df.loc[df['artist'] == 'Bacon, Francis', :]

# Here we're using iloc; with this, you aren't allowed to select label, but rather position, however the syntax is similar..
# df.iloc[row_indexer, column_indexer]
df.iloc[100:300, [0,1,4]]
# So we're selecting from rows 100 to 300, & passing 3 column positions

df.loc[1035, 'artist']
df.iloc[0, 0]
df.iloc[0:2, 0:2]


# Try multiplication: (It won't work here)
df['height'] * df['width']

df['width'].sort_values().head()
df['width'].sort_values().tail()

# Try to convert:
pd.to_numeric(df['width'])

# Force NaNs if the value cannot be converted to a numeric value
pd.to_numeric(df['width'], errors = 'coerce')
df.loc[:, 'width'] = pd.to_numeric(df['width'], errors = 'coerce')

pd.to_numeric(df['height'], errors = 'coerce')
df.loc[:, 'height'] = pd.to_numeric(df['height'], errors = 'coerce')

# Try multiplication now that errors have been resolved & values exist as integers
df['height'] * df['width']

df['width']

df['units'].value_counts()

# Assign new columns with size
area = df['height'] * df['width']
df = df.assign(area = area)

df['area'].max()

df['area'].min()

# Using idxmax (or index max) we can view the index of the biggest value in question
df.loc[df['area'].idxmax(), :]
