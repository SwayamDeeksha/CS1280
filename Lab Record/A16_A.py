import pandas as pd
import matplotlib.pyplot as plt

file_path = '6Mcd.csv'
data = pd.read_csv(file_path)

print(data.head())

variable_name = 'VariableName'
time_column = 'Time'

if variable_name not in data.columns or time_column not in data.columns:
    print(f"Columns '{variable_name}' or '{time_column}' not found in the dataset.")
else:
    plt.figure(figsize=(10, 5))
    plt.plot(data[time_column], data[variable_name], marker='o', label='Trend')
    plt.title(f"Trend of {variable_name}")
    plt.xlabel(time_column)
    plt.ylabel(variable_name)
    plt.legend()
    plt.grid()
    plt.show()

    plt.figure(figsize=(10, 5))
    sns.lineplot(x=time_column, y=variable_name, data=data, marker='o')
    plt.title(f"Trend of {variable_name} (Seaborn)")
    plt.xlabel(time_column)
    plt.ylabel(variable_name)
    plt.grid()
    plt.show()
