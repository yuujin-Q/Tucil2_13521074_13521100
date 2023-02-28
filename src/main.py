from point_set import *
from solver import *
import time
from visualizer import *

def int_input_validation(min, max, prompt):
    valid = False
    result = input(prompt)
    while (not valid):
        try:
            result = int(result)
            if result >= min and result <= max:
                valid = True
            else:
                print("Input must be in between " + str(min) + " and " + str(max) +"!")
                result = input(prompt)
        except:
            print("Input Invalid!")
            result = input(prompt)
    return result


# MAIN FUNCTION
p_set = []
legal = False

# Input Validation
p_dimension = int_input_validation(1, 100, "Input Dimension : ")
p_count = int_input_validation(1, 10000, "Input Amount of Points : ")
min_max = int_input_validation(1, 10000,"Input Maximum & Minimum Value for All Axes : ")
f_prec = int_input_validation(0, 10, "Input Fractional Precision : ")
    

# Add Points and Sort by Each Axes
add_n_rand_point(p_set, p_count, min_max, f_prec, p_dimension)
p_set = quickSort(p_set)

# Display Point Set Information (Points, Dimension, Point Count)
print("\nPOINT SET INFORMATION:")
print_info(p_set)

# Solve by Brute Force and by Divide & Conquer
print("=======BRUTE FORCE SOLUTION========")
timer_bf = time.time_ns()
pair_bf, dist_bf, op_count_bf = closest_pair_bf(p_set)
timer_bf = time.time_ns() - timer_bf
print("Nearest pair :", pair_bf)
print("Distance :", dist_bf)
print("Processing time :", timer_bf / 1000000, "ms")
print("Euclidean Distance Usage Count :", op_count_bf)

print()

print("=====DIVIDE & CONQUER SOLUTION=====")
timer_dnc = time.time_ns()
pair_dnc, dist_dnc, op_count_dnc = closest_pair_dnc(p_set)
timer_dnc = time.time_ns() - timer_dnc
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

# visualise only for 2 and 3 dimension
if (p_dimension>1 and p_dimension<4):
    visualizer(p_dimension, p_set, pair_dnc)