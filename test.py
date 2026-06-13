import pandas as pd

df = pd.read_csv("dataset/retail_sales_data.csv")

print(df.isnull().sum())