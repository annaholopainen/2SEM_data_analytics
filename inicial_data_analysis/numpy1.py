import numpy as np

#salaries from Nice Company Ltd.
salaries = np.arange(1500, 6000, 500)

# increasing each salary by 150
salaries[:] += 150

# adding 10€
salaries[:] = salaries[:] * 1.1