import numpy as np

data = np.arange(1,101)

squares = np.sqrt(data)
# reshape can be used to make tables from a flat data
# to make the opposite (from a table to flat) use ravel
values = np.arange(0,100).reshape(10,10)

total= values.sum()

total_rows = values.sum(axis=1)

total_columns = values.sum(axis=0)

