import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://admin:terminator@database-1.cl0u02ukszrv.ap-south-1.rds.amazonaws.com:3306/retail_sales_db"
)

query1 = """
SELECT
    ROUND(SUM(total_sales),2) as total_revenue
FROM sales
"""

query2 = """
SELECT
    count(*) as total_orders
FROM sales
"""

query3 = """
SELECT
    category,
    sum(total_sales) as total_revenue
from sales
group by category
order by total_revenue desc
"""

print(pd.read_sql(query1, engine))
print(pd.read_sql(query2, engine))
print(pd.read_sql(query3, engine))