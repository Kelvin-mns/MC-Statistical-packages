import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

grouped = df.groupby("Gender")

result = grouped.agg({"Income": ["mean", "sum", "std"]})

print(result)











# print(categories)
# print(gender)









