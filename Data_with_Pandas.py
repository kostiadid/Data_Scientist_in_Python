import pandas as pd

f500 = pd.read_csv("f500.csv")

f500_head = f500.head(10)
print(f500.info())
