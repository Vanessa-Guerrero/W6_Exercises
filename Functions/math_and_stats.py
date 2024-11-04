import random
import math
import statistics

vals_1_100 = range(1,100) 
vals_sample = random.sample(vals_1_100, 75) 
vals_choices = random.choices(vals_1_100, k = 200) 
radius = random.randint(3,10)  
pi = math.pi 

# Additional variables for 

sample_sum = math.fsum(vals_sample)
sample_avg = statistics.mean(vals_sample)
sample_median = statistics.median(vals_sample)

# Additional variables for calculations performed on vals_choices

choices_avg = statistics.mean(vals_choices)  
choices_median = statistics.median(vals_choices)  
choices_mode = statistics.mode(vals_choices)  
choices_stdev = statistics.stdev(vals_choices)  
choices_variance = statistics.variance(vals_choices)  

# Calculating area of a random circle using rand int from radius
area = pi * (radius**2)
area_rounded_up = math.ceil(area)  # Rounding up to nearest integer
area_rounded_down = math.floor(area)  # Rounding down to nearest integer

# Printing output with headers and line breaks
print("_Experimenting with a subset of integers 1-100:")
print(f"Sum of 75 sample values from 1 to 100: {sample_sum}")
print(f"Average of 75 sample values: {sample_avg}")
print(f"Median of 75 sample values: {sample_median}")

print('\n') 

print("_Experimenting with a superset of 200 values, integers 1-100:")
print(f"Average of 200 values: {choices_avg}")
print(f"Median of 200 values: {choices_median}")
print(f"Mode of 200 values: {choices_mode}")
print(f"Standard deviation of 200 values: {choices_stdev}")
print(f"Variance of 200 values: {choices_variance}")

print('\n') 

print("_Modeling a random circle:")
print(f"Radius = {radius}, area = {area_rounded_up} (rounded up to the nearest integer)")
print(f"Radius = {radius}, area = {area_rounded_down} (rounded down to the nearest integer)")



