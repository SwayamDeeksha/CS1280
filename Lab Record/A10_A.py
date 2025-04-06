import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

file_path = '4laptops_Updated_Price.csv'
data = pd.read_csv(file_path)

print("Original Data:")
print(data.head())

one_hot_encoder = OneHotEncoder(sparse=False)
os_encoded = one_hot_encoder.fit_transform(data[['Operating System']])
os_encoded_df = pd.DataFrame(os_encoded, columns=one_hot_encoder.get_feature_names_out(['Operating System']))

label_encoder = LabelEncoder()
data['Storage_Encoded'] = label_encoder.fit_transform(data['Storage'])
data = pd.concat([data, os_encoded_df], axis=1)
data = data.drop(columns=['Operating System', 'Storage'])

print("\nTransformed Data:")
print(data.head())
data.to_csv('4laptops_transformed.csv', index=False)