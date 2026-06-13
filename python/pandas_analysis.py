import pandas as pd

df = pd.read_csv("dataset/retail_sales_data.csv")

category_sales = df.groupby('category')['total_sales'].sum().sort_values(ascending = False)

top_customers = df.groupby('customer_name')['total_sales'].sum().sort_values(ascending = False).head(5)

print("Total_Revenue:", df['total_sales'].sum())

print("Total_Orders:", len(df))

print("Average order value:", df['total_sales'].mean())

print("unique customers:", df['customer_id'].nunique())

print(category_sales)
print(top_customers)
