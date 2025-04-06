import pandas as pd

df = pd.read_csv('4laptops.csv')
q1 = df['screen_size_inches'].quantile(0.25)
q3 = df['screen_size_inches'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
outliers = df[(df['screen_size_inches'] < lower_bound) | (df['screen_size_inches'] > upper_bound)]
print(outliers)