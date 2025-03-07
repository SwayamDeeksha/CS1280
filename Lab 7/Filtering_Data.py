import pandas as pd

# Filter rows where Age > 25
filtered_df = df[df["Age"] > 25]
print(filtered_df)

filtered_df = df[df["Age"].isin([35])] 
print(filtered_df)

df["Age"].isin

# >= will print
print(df["Age"]>25)

# > will print
print(df[df["Age"]>25])
