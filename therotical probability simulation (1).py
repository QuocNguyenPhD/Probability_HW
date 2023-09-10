#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import time
# Record the start time
start_time = time.time()
# Define the constants
proportion_x1 = 0.15
proportion_x2 = 0.4
proportion_x3 = 0.43
total_samples = 500

# Initialize the sum
Pa = 0

# Iterate through possible values of x1, x2, and x3
for x1 in range(0, int(proportion_x1 * total_samples) + 1):
    for x2 in range(0, int(proportion_x2 * total_samples) + 1):
        for x3 in range(int(proportion_x3 * total_samples), total_samples + 1):
            if x1 + x2 + x3 == total_samples:
                # Calculate the term based on the corrected formula
                term = (
                    math.comb(total_samples, x1)
                    * math.comb(total_samples - x1, x2)
                    * math.comb(total_samples - x1 - x2, x3)
                    * ((0.18) ** x1)
                    * ((0.42) ** x2)
                    * ((0.4) ** (500 - x1 - x2))
                )
                # Add the term to the sum
                Pa += term
# Record the end time
end_time = time.time()

# Calculate the total computing time
computing_time = end_time - start_time
# Print the result
print("P(A) =", Pa)
print("computing time =", computing_time)

