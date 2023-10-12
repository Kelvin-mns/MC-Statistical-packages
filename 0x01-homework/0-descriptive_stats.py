#importing the necessary libraries
import numpy as np
import pandas as pd

#reading from the csv file
df = pd.read_csv("data.csv")

income_values = np.array(df["Income"])
final_mean = np.mean(income_values)
final_median = np.median(income_values)
std_dev = np.std(income_values)

#printing out the mean, median and the standard deviation
print("The mean value for the income is: ", final_mean)
print("The median value for the income is: ", final_median)
print("The standard deviation for the income value is: ", std_dev)

