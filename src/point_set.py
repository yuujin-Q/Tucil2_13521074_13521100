"""
:file: point_set.py

set of points and functions used in the closest pair problem
"""

import random

# point set variable
global p_set
p_set = []

def add_point(point):
    """add new point to p_set

    :param point: tuple of numbers
    """
    p_set.append(point)

def add_rand_point(min_max_val, fprecision, dimension = 3):
    """add unique random point to p_set

    :param min_max_val: determines the minimum and maximum value for randomization
    :param fprecision: determines digit count of fractional part
    :param dimension: dimension of point to be added, default = 3
    """
    point = []
    for i in range(dimension):      # create new point
        point.append(round(random.uniform(-min_max_val, min_max_val), fprecision))
    
    if tuple(point) in p_set:       # ensure p_set element uniqueness
        add_rand_point(min_max_val, fprecision, dimension)
    else:
        add_point(tuple(point))

def add_n_rand_point(n, min_max_val, fprecision, dimension = 3):
    """add n amount of randomized points to p_set

    :param n: amount of points to be added
    :param min_max_val: determines the minimum and maximum value for randomization
    :param fprecision: determines digit count of fractional part
    :param dimension: dimension of point to be added, default = 3
    """
    for i in range(n):
        add_rand_point(min_max_val, fprecision, dimension)

def get_info_string():
    """get information about current point set

    :return: string of current point set information
    """
    info = ""
    p_count = len(p_set)

    info += "Number of Points : " + str(p_count) + "\n"
    if p_count > 0:
        info += "Dimension : " + str(len(p_set[0])) + "\n"
        info += "Points :\n"
        for points in p_set:
            info += " " + str(points) + "\n"
    return info

def print_info():
    """prints information of current point set"""
    info = get_info_string()
    print(info)
