"""
:file: main.py

main program for closest pair problem
"""

from point_set import *
from solver import *
import time
from visualizer import *


def int_input_validation(val_min, val_max, prompt):
    """validate integer input

    :param val_min: minimum value for integer input (inclusive)
    :param val_max: maximum value for integer input (inclusive)
    :param prompt: input prompt
    :return: validated integer value
    """
    valid = False
    result = input(prompt)
    while not valid:
        try:
            result = int(result)
            if val_min <= result <= val_max:
                valid = True
            else:
                print("Input must be in between " + str(val_min) + " and " + str(val_max) + "!")
                result = input(prompt)
        except:
            print("Input Invalid!")
            result = input(prompt)
    return result


# **** MAIN FUNCTION ****
p_set = []

# Input Validation
p_dimension = int_input_validation(2, 100, "Input Dimension : ")
p_count = int_input_validation(1, 10000, "Input Amount of Points : ")
min_max = int_input_validation(1, 10000, "Input Maximum & Minimum Value for All Axes : ")
f_precision = int_input_validation(0, 10, "Input Fractional Precision : ")

# Add Points and Sort by Each Axes
add_n_rand_point(p_set, p_count, min_max, f_precision, p_dimension)
p_set = quick_sort(p_set)

print()

# Display Point Set Information (Points, Dimension, Point Count)
show_info_choice = int_input_validation(0, 1, "Show Point Set Information? (1/0) : ")
if show_info_choice == 1:
    print()
    print_point_set_info(p_set)

print()

# Solve by Brute Force and by Divide & Conquer
print("=======BRUTE FORCE SOLUTION========")
timer_bf = time.time_ns()
pair_bf, dist_bf, op_count_bf = closest_pair_bf(p_set)
timer_bf = time.time_ns() - timer_bf
display_solution(pair_bf, dist_bf, op_count_bf, timer_bf)

print()

print("=====DIVIDE & CONQUER SOLUTION=====")
timer_dnc = time.time_ns()
pair_dnc, dist_dnc, op_count_dnc = closest_pair_dnc(p_set)
timer_dnc = time.time_ns() - timer_dnc
display_solution(pair_dnc, dist_dnc, op_count_dnc, timer_dnc)

print()

# Validity Check
if dist_bf == dist_dnc:
    print("SOLUTION VALID")

    # Visualize only for 2 and 3 dimension
    if 1 < p_dimension < 4:
        print("VISUALIZING POINTS (2D/3D)")
        visualizer(p_dimension, p_set, pair_dnc)

else:
    print("SOLUTION INVALID")
