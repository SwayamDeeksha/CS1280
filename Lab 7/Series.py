import pandas as pd
import numpy as np
data = [1, 3, 5, np.nan, 6]
s = pd.Series(data)
s2 = pd.Series((data), index=['a', 'b', 'c', 'd','e'])
print(s2)
