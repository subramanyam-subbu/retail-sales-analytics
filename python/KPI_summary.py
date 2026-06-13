import pandas as pd 

df = pd.read_csv('dataset/retail_sales_data.csv')

total_revenue = df['total_sales'].sum()

total_orders = len(df)

total_customers = df['customer_id'].nunique()

avg_order_value = df['total_sales'].mean()

print("===========EXECUTIVE KPI SUMMARY===========")

print(f"Total Revenue    : {total_revenue:,.2f}")
print(f"Total orders     : {total_orders}")
print(f"Total Customers  : {total_customers}")
print(f"avg_order_value  : {avg_order_value:,.2f}")

