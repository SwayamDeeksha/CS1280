import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('3Salary_Data.csv')
plt.scatter(data['YearsExperience'], data['Salary'])
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Scatter Plot of Years of Experience vs Salary')
plt.show()