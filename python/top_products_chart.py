import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('dataset/retail_sales_data.csv')

top_products = df.groupby('product_name')['total_sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))

top_products.plot(kind='bar')

plt.title("Top 10 Products by Revenue")
plt.xlabel("products")
plt.ylabel('Revenue')

plt.xticks(rotation = 45)
plt.tight_layout()

plt.savefig("reports/top_products.png")

print("Chart created Successfully")
