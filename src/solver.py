"""
:file: solver.py

contains definitions of functions & procedures used in solving the closest pair problem
"""

import math
import time

def euclid_distance(point1, point2):
    """calculate euclidean distance between two points

    :param point1: tuple of numbers
    :param point2: tuple of numbers
    :return: euclidean distance of both points
    """
    return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))

def closest_pair_bf(points):
    """get the closest pair from point set using brute force

    :points: set (list) of points (tuple of numbers)
    :return: closest pair of points, minimum distance, recorded processing time (ns), euclidean distance count
    """
    p_count = len(points)
    min_dist = float('inf')
    nearest_pair = None
    op_count = 0

    start_time = time.time_ns()
    for i in range(p_count - 1):
        for j in range(i + 1, p_count):
            curr_dist = euclid_distance(points[i], points[j])
            op_count += 1
            if curr_dist < min_dist:
                min_dist = curr_dist
                nearest_pair = (points[i], points[j])
    recorded_time = time.time_ns() - start_time

    return nearest_pair, min_dist, recorded_time, op_count

#chore: Divide n Conquer
