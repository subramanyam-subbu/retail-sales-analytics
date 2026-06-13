import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://admin:terminator@database-1.cl0u02ukszrv.ap-south-1.rds.amazonaws.com:3306/retail_sales_db"
)

query = """
SELECT
    DATE_FORMAT(order_date, '%%Y-%%m') as sales_month,
    SUM(total_sales) as total_revenue
FROM sales
GROUP BY sales_month
ORDER BY sales_month
"""

df = pd.read_sql(query,engine)

print(df)