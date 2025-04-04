import pandas as pd

file_path = "2Experience.csv"

try:
    df = pd.read_csv(file_path)
    
    print("First 5 rows of the DataFrame:")
    print(df.head())

    print("\nLast 3 rows of the DataFrame:")
    print(df.tail(3))
    
    print("\nDescription of numeric columns in the DataFrame:")
    print(df.describe())

    print("\nInformation about the DataFrame:")
    df.info()

    print("\nColumn names of the DataFrame:")
    print(df.columns)

except FileNotFoundError:
    print(f"Error: The file '{file_path}' could not be found. Please verify the path and file name.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")