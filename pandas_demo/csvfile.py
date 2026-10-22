import pandas_demo as pd

customers = pd.read_csv('customer.csv')
print(customers)
customers.to_csv('customers.csv', index=False)