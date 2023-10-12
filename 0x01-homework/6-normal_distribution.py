from scipy.stats import norm
import numpy as np

mean = 78
std_dev = 25
total_student = 100
score = 70

z_score = (score - mean) / std_dev

prob = norm.cdf(z_score)

percent = (1 - prob) * 100

print(percent)