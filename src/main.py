from point_set import *
from solver import *

# MAIN FUNCTION
p_dimension = int(input("Input Dimension : "))
p_count = int(input("Input Amount of Points : "))

add_n_rand_point(p_count, 5, 1, p_dimension)

# sort
print("\nPOINT SET INFORMATION:")
print_info()

print("=====BRUTE FORCE SOLUTION=====")
pair, dist, timer, op_count = closest_pair_bf(p_set)
print("Nearest pair :", pair)
print("Distance :", dist)
print("Processing time :", timer / 1000000, "ms")
print("Euclidean Distance Usage Count :", op_count)

# print result (divide&conquer vs bruteforce)
# show solve time

# log

# visualise
