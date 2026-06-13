import pandas as pd
from sqlalchemy import create_engine

#Read CSV

df = pd.read_csv("dataset/retail_sales_data.csv")

#RDS connection

engine = create_engine(
    "mysql+pymysql://admin:terminator@database-1.cl0u02ukszrv.ap-south-1.rds.amazonaws.com:3306/retail_sales_db"
)

#load CSV

df.to_sql(
    name = "sales",
    con = engine,
    if_exists = "append",
    index = False
)

print("data loaded Successfully")
print("Total Records:", len(df))