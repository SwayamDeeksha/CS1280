import pandas as pd
data = pd.read_csv("6Mcd_null_values.csv")

null_values = data.isnull().sum()
print("Null values in each column:")
print(null_values)

data_cleaned = data.drop_duplicates()

data_cleaned.to_csv("6Mcd_cleaned.csv", index=False)

print("\nDuplicates dropped. Cleaned dataset saved as '6Mcd_cleaned.csv'.")