import pandas as pd
import numpy as np

#reading the data from the csv file.
df = pd.read_csv("data.csv")

incomes = np.array(df["Income"])

#calculating the 26th percentile. 
q1 = np.percentile(incomes, 25)

#calculating the 75th percentile.
q2 =np.percentile(incomes, 75)

#calculating the median or the 50th percentile.
median = np.median(incomes)

#printing out the 25th percentile, 75th percentile and the 50th percentile or the median.
print("The 25th percentile is: ", q1)
print("The 75th percentile is: ", q2)
print("The median or the 50th percentile is: ", median)