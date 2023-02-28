"""
:file: solver.py

contains definitions of functions & procedures used in solving the closest pair problem
"""

import math

def euclid_distance(point1, point2):
    """calculate euclidean distance between two points

    :param point1: tuple of numbers
    :param point2: tuple of numbers
    :return: euclidean distance of both points
    """
    return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))

"""Sorting Algorithm"""
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    l_arr = arr[:mid]
    r_arr = arr[mid:]
    
    l_arr = mergeSort(l_arr)
    r_arr = mergeSort(r_arr)
    
    return merge(l_arr, r_arr)
    
def merge(l_arr, r_arr):
    res = []
    i=0
    j = 0
    
    while i < len(l_arr) and j < len(r_arr):
        if l_arr[i] < r_arr[j]:
            res.append(l_arr[i])
            i += 1
        else:
            res.append(r_arr[j])
            j += 1
    res += l_arr[i:]
    res += r_arr[j:]
    
    return res

def quickSort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    l_arr = []
    r_arr = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            l_arr.append(arr[i])
        else:
            r_arr.append(arr[i])
    return quickSort(l_arr) + [pivot] + quickSort(r_arr)


    
def closest_pair_bf(points):
    """get the closest pair from point set using brute force

    :points: set (list) of points (tuple of numbers)
    :return: closest pair of points, minimum distance, euclidean distance count
    """
    p_count = len(points)
    min_dist = float('inf')
    nearest_pair = []
    op_count = 0

    for i in range(p_count - 1):
        for j in range(i + 1, p_count):
            curr_dist = euclid_distance(points[i], points[j])
            op_count += 1
            if curr_dist < min_dist:
                min_dist = curr_dist
                nearest_pair = []
            if curr_dist <= min_dist:
                nearest_pair.append((points[i], points[j]))

    return nearest_pair, min_dist, op_count

def closest_pair_dnc(points):
    """get the closest pair from point set using divide and conquer

    :points: set (list) of points (tuple of numbers)
    :return: closest pair of points, minimum distance, euclidean distance count
    """
    p_count = len(points)
    dimension = len(points[0])
    if (p_count <= 3):
        return closest_pair_bf(points)
    else:
        imedian = p_count // 2
        median_point = points[imedian]
        pair1, dist1, ecount1 = closest_pair_dnc(points[:imedian])
        pair2, dist2, ecount2 = closest_pair_dnc(points[imedian:])
        
        min_dist = min(dist1, dist2)
        min_pair = []
        if dist1 != dist2:
            min_pair = pair1 if min_dist == dist1 else pair2
        else:
            min_pair = pair1 + pair2

        total_ecount = ecount1 + ecount2
        
        delta_strip = []
        for p in points:
            if abs(p[0] - median_point[0]) < min_dist:
                delta_strip.append(p)
        
        delta_count = len(delta_strip)
        for i in range(delta_count):
            for j in range(i + 1, delta_count):
                within_delta = True
                for axis in range(1, dimension):
                    within_delta = within_delta and abs(delta_strip[i][axis] - delta_strip[j][axis]) < min_dist

                if within_delta:
                    dist3 = euclid_distance(delta_strip[i], delta_strip[j])
                    total_ecount += 1
                    
                    if dist3 < min_dist:
                        min_dist = dist3
                        min_pair = []
                    if dist3 <= min_dist:
                        min_pair.append((delta_strip[i], delta_strip[j]))
        
        return min_pair, min_dist, total_ecount


