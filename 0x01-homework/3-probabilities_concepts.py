import numpy as np

np.random.seed(0)
dice_rolls = np.random.choice([1, 2, 3, 4, 5], size=100)

event_A = dice_rolls > 4

event_B = dice_rolls % 2 != 0

event_A_intersect_B = event_A & event_B
prob_A_intersect_B = event_A_intersect_B.sum() / 100

prob_B = event_B.sum() / 100

prob_A_given_B = prob_A_intersect_B / prob_B
print(prob_A_given_B)