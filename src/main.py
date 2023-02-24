from point_set import PointSet

# MAIN FUNCTION
dimension = int(input("Input Dimension : "))
point_count = int(input("Input Amount of Points : "))

print("\nInformation :")
point_set = PointSet(dimension)
point_set.add_n_rand_point(point_count, 5, 1)

# sort

point_set.print_info()

pair, dist, timer = point_set.nearest_pair_bf()
print("Nearest pair :", pair)
print("Distance :", dist)
print("Processing time :", timer, "ns")

# print result (divide&conquer vs bruteforce)
# show solve time

# log

# visualise
