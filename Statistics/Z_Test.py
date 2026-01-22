import numpy as np
import pandas as pd
from scipy.stats import norm

sample = [
    48, 50, 52, 49, 51, 50, 53, 47, 54, 49,
    50, 52, 51, 48, 49, 53, 50, 51, 52, 48,
    49, 50, 54, 51, 52, 49, 50, 51, 48, 53
]

population_mean= 50
population_std = 2
alpha = 0.05
sample_size =  len(sample)
sample_mean = np.mean(sample)
z_score =  round(( sample_mean - population_mean ) / ( population_std / np.sqrt(sample_size) ),2)
print(f"Z-Score  : {z_score}")
# uisng critical z-values : we check either z_score lies between the range of significant values or not )

# using p_values : 
p_value = 2 * ( 1- norm.cdf(z_score))
print(f"P_Score : {round(p_value,2)}")

if p_value < alpha :
    print("Reject The Null Hypothesis")
    print(f"Reason : p_value {round(p_value,2)} is less than z_score {z_score}")
else : 
    print("Accept the Null Hypothesis")
    print(f"Reason : p_value {round(p_value,2)} is greater than z_score {z_score}")