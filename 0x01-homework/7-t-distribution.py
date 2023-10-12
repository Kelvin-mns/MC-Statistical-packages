from scipy import stats
import pandas as pd

df = pd.DataFrame({
    "data_column": [23, 24, 25, 21, 20, 24, 23, 30, 36, 28,]
})

mu = df["data_column"].mean()
sigma = df["data_column"].std()

sem = stats.sem(df["data_column"])

confidence = 0.95
ci = stats.t.interval(confidence, len(df["data_column"] - 1, loc=mu, scale=sem))

print(ci)


