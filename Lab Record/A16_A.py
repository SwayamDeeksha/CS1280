import pandas as pd
import matplotlib.pyplot as plt

file_path = '6Mcd.csv'
data = pd.read_csv(file_path)

print(data.head())

variable_name = 'VariableName'
time_column = 'Time'