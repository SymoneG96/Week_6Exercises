import random
import math
import statistics

# Starting variables
vals1_100 = range(1, 100)
vals_sample = random.sample(vals1_100, 75)
vals_choices = random.choices(vals1_100, k=200)
radius = random.randint(3, 10)
pi = math.pi

# Calculations for the subset
sum_sample = sum(vals_sample)
avg_sample = statistics.mean(vals_sample)
median_sample = statistics.median(vals_sample)

# Calculations for the superset
avg_choices = statistics.mean(vals_choices)
median_choices = statistics.median(vals_choices)
mode_choices = statistics.mode(vals_choices)
stdev_choices = statistics.stdev(vals_choices)
variance_choices = statistics.variance(vals_choices)

# Calculations for the circle
area = pi * (radius ** 2)
area_rounded_up = math.ceil(area)
area_rounded_down = math.floor(area)

# Output
print("_Experimenting with a subset of integers 1-100:")
print("Sum of 75 sample values from 1 to 100:", sum_sample)
print("Average of 75 sample values:", avg_sample)
print("Median of 75 sample values:", median_sample)

print("\n_Experimenting with a superset of 200 values, integers 1-100:")
print("Average of 200 values:", avg_choices)
print("Median of 200 values:", median_choices)
print("Mode of 200 values:", mode_choices)
print("Standard deviation of 200 values:", stdev_choices)
print("Variance of 200 values:", variance_choices)

print("\n_Modeling a random circle:")
print("Radius =", radius, ", area =", area_rounded_up, "(rounded up to the nearest integer)")
print("Radius =", radius, ", area =", area_rounded_down, "(rounded down to the nearest integer)")