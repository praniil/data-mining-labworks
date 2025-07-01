import pandas as pd

ecommerce_data = { 
'OrderID': [101, 102, 103, 104, 105, 106, 107], 
'CustomerName': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'], 
'Category': ['Electronics', 'Fashion', 'Electronics', 'Home', 'Fashion', 'Electronics', 'Home'], 
'Amount': [200, 150, 300, 400, 250, 500, 350], 
'Discount': [20, 10, 30, 50, 20, 60, 40], 
'PurchaseDate': pd.to_datetime(['2023-11-20', '2023-11-21', '2023-11-22', '2023-11-23', '2023-11-24', '2023-11-25', '2023-11-26']), 
'City': ['New York', 'Los Angeles', 'New York', 'Chicago', 'Los Angeles', 'Chicago', 'New York'] 
}

df = pd.DataFrame(ecommerce_data)
print(df.shape)

print(df.isnull().sum)

#fetch rows for orders placed by customers from New York
print(df.head())

print(df[df['City'] == "New York"])
print(df['Amount'].mean())
print(df['Discount'].sum())

print(df[(df['Category'] == "Electronics") & (df['Amount'] > 250)])

print(df.loc[:3, ['CustomerName', 'Amount']])

print(df.iloc[:3, 1:3])

#retrieve [Charlie Electronics 300] using loc and iloc
print(df.iloc[2:3, 1:4])
print(df.loc[2:2, ['CustomerName', 'Category', 'Amount']])

print(df['City'].replace(to_replace = "New York", value=df['City'].mode()))

