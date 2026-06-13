import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('dataset/retail_sales_data.csv')

state_sales = df.groupby('state')['total_sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))

state_sales.plot(kind='bar')

plt.title('Revenue by State')
plt.xlabel('States')
plt.ylabel('Revenue')

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("reports/state_by_revenue.png")

print("chart created successfully")