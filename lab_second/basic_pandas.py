import pandas as pd

d = {
    "name": ["Pranil", "Anusha", "Shane", "Virat"],
    "age": [22, 16, 33, None]
}

df = pd.DataFrame(d)
print(df.head())
print(df.tail())

print(df.columns)
df.isnull().sum()

df["age"] = df["age"].fillna(2)
print(df.tail())
