import numpy as np
from scipy import stats


data = np.random.randint(150, 190, [10, 10])

mean = data.mean()

median = np.median(data)

moda = stats.mode(data).mode[0]

maximum = np.max(data)

minimum = np.min(data)

delta = maximum - minimum

dispers = np.var(data)

sko = np.std(data)

print(sko)
