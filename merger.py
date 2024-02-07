import pandas as pd
import os

# Life is so much easier in python... 
path = os.path.join(os.getcwd(), "df1.csv")
path2 = os.path.join(os.getcwd(), "df2.csv")
path3 = os.path.join(os.getcwd(), "df3.csv")
data = pd.read_csv(path)
data2 = pd.read_csv(path2)
data["price"] = data2["price"]
print(data.head(5))

data.to_csv(path3)