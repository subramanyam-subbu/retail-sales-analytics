import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset/retail_sales_data.csv')

df["order_date"] = pd.to_datetime(df['order_date'])

monthly_sales = df.groupby(df['order_date'].dt.strftime("%Y-%m"))['total_sales'].sum()

plt.figure(figsize=(10,5))

monthly_sales.plot(kind="line")

plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig('reports/monthly_revenue_trend.png')

print("chart created successfully")