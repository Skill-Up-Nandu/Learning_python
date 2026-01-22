# A health researchers claims that the average weight of adult males in a city is 70 kg.
# A sample of 49 men is taken and their avg weight is found to be 72kg.
# Assume population std is 8kn
# At 5% significant level, test the claim using a one sample z_test.
# explain the question


# Null hypothesis (H₀): μ = 70

# Alternative hypothesis (H₁): μ != 70


import numpy as np
import pandas as pd
from scipy.stats import norm
pop_mean = 70
pop_std = 8
sample_mean = 72
sample_size = 49
alpha = 0.05
z_score = (sample_mean - pop_mean)/(pop_std/(np.sqrt(sample_size)))
print(z_score)
p_value = 2 * (1 - norm.cdf(abs(z_score)))
print(round(p_value,2))

if p_value < alpha :
    print("Reject The Null Hypothesis")
    print(f"Reason : p_value {round(p_value,2)} is less than aplpa {alpha}")
else : 
    print("Accept the Null Hypothesis")
    print(f"Reason : p_value {round(p_value,2)} is greater than alpha {alpha}")