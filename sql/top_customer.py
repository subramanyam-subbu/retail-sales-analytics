import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://admin:terminator@database-1.cl0u02ukszrv.ap-south-1.rds.amazonaws.com/retail_sales_db"
)

query = """
SELECT 
    customer_name,
    SUM(total_sales) as total_revenue
FROM sales
GROUP BY customer_name
ORDER By total_revenue desc
LIMIT 10
"""

df = pd.read_sql(query, engine)

print(df)