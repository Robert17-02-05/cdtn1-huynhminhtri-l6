import pandas as pd

df = pd.read_csv('data/sample/stores.csv')
print("Số dòng, số cột:", df.shape)
print("--- 5 dòng đầu ---")
print(df.head())