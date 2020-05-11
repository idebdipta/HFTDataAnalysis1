import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#fig = plt.figure(figsize=plt.figaspect(0.5))

df = pd.read_csv('FT.csv', dayfirst=True, index_col=0)

df.plot()
plt.show()