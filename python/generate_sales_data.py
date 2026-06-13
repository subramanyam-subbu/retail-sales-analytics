import pandas as pd 
import random
from datetime import datetime, timedelta

customers = [
     "John", "David", "Alice", "Robert", "Emma",
    "Sophia", "James", "Michael", "William", "Olivia"
]

cities = [
     "Hyderabad", "Bangalore", "Chennai",
    "Mumbai", "Pune", "Delhi"
]

states = [
    "Telangana", "Karnataka", "Tamil Nadu",
    "Maharashtra", "Delhi"
]

categories = {
    "Electronics":[
        "Laptop",
        "Mouse",
        "Keyboard",
        "Monitor"
    ],
    "Furniture": [
        "Chair",
        "Desk",
        "Table"
    ],
    "Accessories": [
        "Headphones",
        "USB Cable",
        "Webcam"
    ]
}

data = []

start_date = datetime(2024,1,1)

for order_id in range(1,5001):

    category = random.choice(list(categories.keys()))

    product = random.choice(categories[category])

    quantity = random.randint(1,10)

    unit_price = random.randint(500,50000)

    total_sales = quantity * unit_price

    order_date = start_date + timedelta(
        days = random.randint(0,730)
    )

    data.append(
        {
            "order_id": order_id,
            "order_date": order_date.date(),
            "customer_id": random.randint(1001,1100),
            "customer_name": random.choice(customers),
            "city": random.choice(cities),
            "state": random.choice(states),
            "category": category,
            "product_name": product,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_sales": total_sales
        }
    )

df = pd.DataFrame(data)

df.to_csv(
    "dataset/retail_sales_data.csv",
    index = False
)

print("Dataset Generated Successfully")
print("Total Records:", len(df))

