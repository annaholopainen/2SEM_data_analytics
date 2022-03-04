import numpy as np

data = np.arange(1,21)

result = data + data

result = data - data 
#goes to each value and does the operation with the corresponding value 


#generates a bunch of ones and uses broadcast to multiply
#ex; multiplies by 5 every "one" generated 
# and np.ones generates float numbers
numbers = np.ones(10)*5

#forcing them to be integers
numbers = np.ones(10, dtype = int)