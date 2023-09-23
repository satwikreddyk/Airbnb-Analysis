import pymongo
import pandas as pd

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["AirBNB"]
collection = db["Data"]

data = list(collection.find({}))
df = pd.DataFrame(data)

df.drop_duplicates(inplace=True)

df.fillna({'price': 0}, inplace=True)
df['price'] = df['price'].astype(float)
average_price_by_property_type = df.groupby('property_type')['price'].mean()

