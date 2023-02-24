from point_set import PointSet

# MAIN FUNCTION
dimension = int(input("Input Dimension : "))
point_count = int(input("Input Amount of Points : "))

point_set = PointSet(dimension)
point_set.add_n_rand_point(point_count, 5, 1)

# sort
print("\nPOINT SET INFORMATION:")
point_set.print_info()

print("BRUTE FORCE SOLUTION")
pair, dist, timer, op_count = point_set.nearest_pair_bf()
print("Nearest pair :", pair)
print("Distance :", dist)
print("Processing time :", timer, "seconds")
print("Euclidean Distance Usage Count :", op_count)

# print result (divide&conquer vs bruteforce)
# show solve time

# log

# visualise
