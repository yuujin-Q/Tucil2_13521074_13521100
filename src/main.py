from point_set import *
from solver import *

# MAIN FUNCTION
p_set = []

# Input Restrictions
p_dimension = int(input("Input Dimension : "))
p_count = int(input("Input Amount of Points : "))
min_max = int(input("Input Maximum & Minimum Value for All Axes : "))
f_prec = int(input("Input Fractional Precision : "))

# Add Points and Sort by Each Axes
add_n_rand_point(p_set, p_count, min_max, f_prec, p_dimension)
p_set = sorted(p_set)

# Display Point Set Information (Points, Dimension, Point Count)
print("\nPOINT SET INFORMATION:")
print_info(p_set)

# Solve by Brute Force and by Divide & Conquer
print("=======BRUTE FORCE SOLUTION========")
pair_bf, dist_bf, timer_bf, op_count_bf = closest_pair_bf(p_set)
print("Nearest pair :", pair_bf)
print("Distance :", dist_bf)
print("Processing time :", timer_bf / 1000000, "ms")
print("Euclidean Distance Usage Count :", op_count_bf)

print()

print("=====DIVIDE & CONQUER SOLUTION=====")
pair_dnc, dist_dnc, timer_dnc, op_count_dnc = closest_pair_dnc(p_set)
print("Nearest pair :", pair_dnc)
print("Distance :", dist_dnc)
print("Processing time :", timer_dnc / 1000000, "ms")
print("Euclidean Distance Usage Count :", op_count_dnc)

print()

# Validity Check
if (dist_bf == dist_dnc):
    print("SOLUTION VALID")
else:
    print("SOLUTION INVALID")

# log

# visualise
