# A company claims that its new software bug fix takes no more than 30 minutes on average.
# A sample of 36 fixes shows an average time of 32 minutes.
# Population standard deviations is known to be 6 minutes .
# Test the company's claim at the 0.01 significance level.


# Null Hypothesis (Ho) :  μ <= 30
# Alter Hypothesis (H1) : μ > 30

import numpy as np
import pandas as pd
from scipy.stats import norm

pop_mean = 30
pop_std = 6
sam_mean = 32
sam_size = 36
alpha = 0.01
z_score = (sam_mean - pop_mean) / (pop_std/np.sqrt(sam_size))
print(z_score)

#  for one tailed test
p_value = 1 - norm.cdf(z_score)

if p_value < alpha : 
    print("Reject The Null Hypothesis")
    print(f"Reason : p_value {p_value:.4f} is less than aplpa {alpha}")
else : 
    print("Fail To Reject the Null Hypothesis")
    print(f"Reason : p_value {p_value:.4f} is greater than alpha {alpha}")