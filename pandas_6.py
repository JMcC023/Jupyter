# Here we'll output data in various formats e.g. Excel, SQL, JSON
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
                 
# Smaller object for easier visualization 
small_df = df.iloc[49980:50019, :].copy()

# Basic Excel
small_df.to_excel("basic.xlsx")
small_df.to_excel("no_index.xlsx", index = False)
small_df.to_excel("columns.xlsx", columns = ["artist", "title", "year"])

# Multiple worksheets
writer = pd.ExcelWriter('multiple_sheets.xlsx', engine = 'xlsxwriter')
small_df.to_excel(writer, sheet_name = "Preview", index = False)
df.to_excel(writer, sheet_name = "Complete", index = False)
writer.save()

# Conditional formatting..
artist_counts = df['artist'].value_counts()
artist_counts.head()
writer = pd.ExcelWriter('colors.xlsx', engine = 'xlsxwriter')
artist_counts.to_excel(writer, sheet_name = "Artist Counts")
sheet = writer.sheets['Artist Counts']

cells_range = 'B2:B{}'.format(len(artist_counts.index))
sheet.conditional_format(cells_range, {'type': '2_color_scale',
                                      'min_value': '10',
                                      'min_type': 'percentile',
                                      'max_value': '99',
                                      'max_type': 'percentile'})
writer.save()
