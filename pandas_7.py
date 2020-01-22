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
                 
# Simplest default plot
# First count how many artworks were provided in a given year
acquisition_years = df.groupby('acquisitionYear').size()
acquisition_years.plot()

# Leveraging Matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({'figure.autolayout' : True,
                 'axes.titlepad': 20})
                 
fig = plt.figure()
subplot = fig.add_subplot(1,1,1)
acquisition_years.plot(ax = subplot)
fig.show()

# Adding axis labels..
fig = plt.figure()
subplot = fig.add_subplot(1,1,1)
# Rotating ticks
acquisition_years.plot(ax=subplot, rot = 45)
subplot.set_xlabel("Acquisition Year")
subplot.set_ylabel("Artworks Acquired")
fig.show()

# Increase ticks granularity
subplot.locator_params(nbins = 40, axis = 'x')

fig.show()

# Add a log scale & a grid
fig = plt.figure()
subplot = fig.add_subplot(1,1,1)
# Rotating ticks
acquisition_years.plot(ax=subplot, rot = 45, logy = True, grid = True)
subplot.set_xlabel("Acquisition Year")
subplot.set_ylabel("Artworks Acquired")
fig.show()

# Can also set fonts..
title_font = {'family': 'source sans pro',
             'color': 'darkblue',
             'weight': 'normal',
             'size' : 20}

labels_font = {'family': 'consolas',
             'color': 'darkred',
             'weight': 'normal',
             'size' : 16}
             
# Add a log scale & a grid
fig = plt.figure()
subplot = fig.add_subplot(1,1,1)
# Rotating ticks
acquisition_years.plot(ax=subplot, rot = 45, logy = True, grid = True)
subplot.set_xlabel("Acquisition Year", fontdict = labels_font, labelpad = 10)
subplot.set_ylabel("Artworks Acquired", fontdict = labels_font)

subplot.set_title("Tate Gallery Acquisitions", fontdict = title_font)
fig.show()

# Save to a file?
fig.savefig('plot.png')
# SVG - vector graphs..
fig.savefig('plot.svg', format = 'svg')
