import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(average_price_by_property_type.index, average_price_by_property_type.values)
plt.xlabel('Property Type')
plt.ylabel('Average Price')
plt.title('Average Airbnb Prices by Property Type')
plt.xticks(rotation=45)
plt.show()