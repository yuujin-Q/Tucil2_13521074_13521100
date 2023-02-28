"""
:file: point_set.py

set of points functions used in the closest pair problem
"""

import random


def add_point(p_set, point):
    """add new point to p_set

    :param p_set: set of point(s)
    :param point: tuple of numbers
    """
    p_set.append(point)


def add_rand_point(p_set, min_max_val, f_precision, dimension=3):
    """add unique random point to p_set

    :param p_set: set of point(s)
    :param min_max_val: determines the minimum and maximum value for randomization
    :param f_precision: determines digit count of fractional part
    :param dimension: dimension of point to be added, default = 3
    """
    point = []
    for i in range(dimension):  # create new point
        point.append(round(random.uniform(-min_max_val, min_max_val), f_precision))

    if tuple(point) in p_set:  # ensure p_set element uniqueness
        add_rand_point(p_set, min_max_val, f_precision, dimension)
    else:
        add_point(p_set, tuple(point))


def add_n_rand_point(p_set, n, min_max_val, f_precision, dimension=3):
    """add n amount of randomized points to p_set

    :param p_set: set of point(s)
    :param n: amount of points to be added
    :param min_max_val: determines the minimum and maximum value for randomization
    :param f_precision: determines digit count of fractional part
    :param dimension: dimension of point to be added, default = 3
    """
    for i in range(n):
        add_rand_point(p_set, min_max_val, f_precision, dimension)


def print_point_set_info(p_set):
    """print information about point set

    :param p_set: set of point(s)
    """
    p_count = len(p_set)

    print("POINT SET INFORMATION:")
    print("Number of Points : " + str(p_count))
    if p_count > 0:
        print("Dimension : " + str(len(p_set[0])))
        print("Points :")
        for points in p_set:
            print(" " + str(points))
