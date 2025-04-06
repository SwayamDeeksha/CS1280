import pandas as pd
data = [
    {"Product Name": "Panda Plush Toy", "Category": "Toys", "Price": 20.0},
    {"Product Name": "Panda Mug", "Category": "Kitchenware", "Price": 15.0},
    {"Product Name": "Panda T-Shirt", "Category": "Clothing", "Price": 25.0},
    {"Product Name": "Panda Notebook", "Category": "Stationery", "Price": 10.0}
]
df = pd.DataFrame(data)
df["Discounted Price"] = df["Price"] * 0.9
print(df)