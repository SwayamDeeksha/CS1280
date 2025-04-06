import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('5ds_salaries.csv')
sns.barplot(x='categorical_column', y='numerical_column', data=df)
plt.xticks(rotation=45)
plt.show()