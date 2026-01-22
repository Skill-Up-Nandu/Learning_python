# It is believe that the average score in satatistic exam is 75.
# Professor think students this year performed worse.
# A random sample of 40 students shows an average score of 72, with a population standard deviation of 10.
# Test the professor's believe at 0.05 significance level.
import numpy as np 
import pandas as pd
from scipy.stats import norm
pop_mean = 75
pop_std = 10
sam_mean = 72
sam_size = 40
alpha = 0.05

# Null Hypothesis  (Ho) : μ = 75 
# Alter Hypothesis (H1) : μ < 75

z_score = (sam_mean - pop_mean) / (pop_std / np.sqrt(sam_size))
print(f"{z_score:.2f}")

p_value = norm.cdf(z_score)

if p_value < alpha : 
    print("Reject The Null Hypothesis")
    print(f"Reason : p_value {p_value:.2f} is less than aplpa {alpha}")
else : 
    print("Fail To Reject the Null Hypothesis")
    print(f"Reason : p_value {p_value:.2f} is greater than alpha {alpha}")