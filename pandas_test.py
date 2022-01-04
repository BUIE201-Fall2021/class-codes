import numpy as np

x = np.array([1,2,3])
y = np.array([3,1,5])

s = np.sum(x)
print(s)
w = np.dot(x, y)
print(w)

import pandas as pd

df = pd.read_csv("cereals.csv")

df.head()

df.describe()

df.plot()

df.plot(kind='box', rot=45)
