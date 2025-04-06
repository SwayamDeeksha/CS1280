import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('5ds_salaries.csv')

print(data.head())

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.histplot(data['salary'], kde=True, bins=30, color='blue')
plt.title('Salary Distribution', fontsize=16)
plt.xlabel('Salary', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x=data['salary'], color='green')
plt.title('Salary Boxplot', fontsize=16)
plt.xlabel('Salary', fontsize=12)
plt.show()
