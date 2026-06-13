import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://admin:terminator@database-1.cl0u02ukszrv.ap-south-1.rds.amazonaws.com:3306/retail_sales_db"
)

query = """
SELECT 
    state,
    SUM(total_sales) as total_revenue
FROM sales
GROUP BY state
ORDER BY total_revenue desc
"""
df = pd.read_sql(query,engine)

print(df)