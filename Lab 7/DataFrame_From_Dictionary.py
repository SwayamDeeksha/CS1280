import pandas as pd
# Create a DataFrame from a dictionary
data = {
    "Name": ["Ram", "Robert", "Rahim"],
    "Age": [25, 30, 35],
    "City": ["Ayodya", "Chennai", "Delhi"],
}
df = pd.DataFrame(data)
print(df)
type(df)
print(data.values(), type(data.values()))
print(df.index, type(df.index))
