import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

data = pd.read_csv('4laptops.csv')
plt.figure(figsize=(10, 6))
sns.boxplot(data=data)
plt.xticks(rotation=45)
plt.show()