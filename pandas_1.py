# Simply import the numpy library
import numpy as np

# Instantiate a random array with 3 elements
numpy_array = np.random.rand(3)

print(numpy_array)
# returns [0.16889049 0.30813743 0.43035289]

# To confirm the type of the array..
type(numpy_array)
# numpy.ndarray

# Now import pandas
import pandas as pd

series = pd.Series(numpy_array)

# The difference between Series & ndarray (n-dimensional) is that in Series, 
# there is an index which can be labelled with our own custom names, as well as basic integer indexing i.e. numpy_array[0]

series = pd.Series(numpy_array, index = ["First", "Second", "Third"])

# Simply outputting the series gives you its details
series

# First     0.705252
# Second    0.677136
# Third     0.443160
# dtype: float64

# The index can be viewed also
series.index

# Index(['First', 'Second', 'Third'], dtype='object')

# Can also move to 2D arrays - 3 rows, 2 columns 
array_2d = np.random.rand(3, 2)

#array([[0.15757754, 0.48581725],
#       [0.26186889, 0.68359588],
#       [0.60441535, 0.06154021]])

array_2d[0,0]
# 0.15757754182025208

# Can also construct a data frame
df = pd.DataFrame(array_2d)

df

# 0	          1
# 0	0.157578	0.485817
# 1	0.261869	0.683596
# 2	0.604415	0.061540

df.columns
# RangeIndex(start=0, stop=2, step=1)

# Specify the indexes like so..
df.columns = ["First", "Second"]

df

#   First	    Second
# 0	0.157578	0.485817
# 1	0.261869	0.683596
# 2	0.604415	0.061540

# Can then access e.g. the 2nd column..
df["Second"]

# 0    0.485817
# 1    0.683596
# 2    0.061540
# Name: Second, dtype: float64

