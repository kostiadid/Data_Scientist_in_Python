import pandas as pd
f500 = pd.read_csv('f500.csv', index_col=0)
f500.index.name = None

f500_shape = f500.shape
print(f500_shape)


f500_type = type(f500)

#  titles    on top  and a side 
f500_top_6= f500.head(6)
f500_bottom_8=f500.tail(8)


#info
print(f500.info())
float64_dtype = 3
int64_dtype = 7
object_dtype = 6

#type function
industries = f500['industry']
industries_type = type(industries)

