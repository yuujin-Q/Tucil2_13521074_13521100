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
def closest_pair_dnc_2d(points):
    p_count = len(points)
    if (p_count <= 3):
        return closest_pair_bf(points)
    else:
        total_time = time.time_ns()
        imedian = p_count // 2
        median_point = points[imedian]
        pair1, dist1, temp, ecount1 = closest_pair_dnc_2d(points[:imedian])
        pair2, dist2, temp, ecount2 = closest_pair_dnc_2d(points[imedian:])
        
        min_dist = min(dist1, dist2)
        min_pair = pair1 if min_dist == dist1 else pair2
        total_ecount = ecount1 + ecount2
        
        delta_strip = []
        for p in points:
            if abs(p[0] - median_point[0]) < min_dist:
                delta_strip.append(p)
        
        delta_count = len(delta_strip)
        for i in range(delta_count):
            for j in range(i + 1, delta_count):
                if abs(delta_strip[i][1] - delta_strip[j][1]) < min_dist:
                    dist3 = euclid_distance(delta_strip[i], delta_strip[j])
                    total_ecount += 1
                    
                    if dist3 < min_dist:
                        min_dist = dist3
                        min_pair = (delta_strip[i], delta_strip[j])

        
        return min_pair, min_dist, time.time_ns() - total_time, total_ecount