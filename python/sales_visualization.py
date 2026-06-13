import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('dataset/retail_sales_data.csv')

category_sales = df.groupby('category')['total_sales'].sum().sort_values(ascending = False)

plt.figure(figsize=(8,5))

category_sales.plot(kind='bar')

plt.title("Revenue By Category")
plt.xlabel('category')
plt.ylabel('Revenue')

plt.tight_layout()

plt.savefig("reports/category_revenue.png")

print("Chart saved Successfully")