import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('5ds_salaries.csv')
sns.barplot(x = 'salary_currency', y='salary_in_usd', data=df)
plt.xticks(rotation=45)
plt.show()
