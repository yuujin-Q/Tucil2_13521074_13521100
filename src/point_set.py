import math
import random
import time


class PointSet:
    DEBUG = False

    def __init__(self, dimension):
        """PointSet constructor

        :param dimension: the dimension for points in the set
        """
        self.p_dimension = dimension
        self.p_set = []
        self.p_count = 0

    def add_point(self, point):
        """add new point to p_set

        :param point: tuple of numbers, dimension of point is p_dimension
        """
        if len(point) == self.p_dimension:
            self.p_set.append(point)
            self.p_count += 1

            if self.DEBUG:
                print("Point Added! Point Count : " + str(self.p_count))

        elif self.DEBUG:
            print("Invalid Point Dimension!")

    def add_rand_point(self, min_max_val, precision):
        """add unique random point to p_set

        :param min_max_val: determines the minimum and maximum value for randomization
        :param precision: determines digit count of fractional part
        """
        point = []
        for i in range(self.p_dimension):
            point.append(round(random.uniform(-min_max_val, min_max_val), precision))

        if tuple(point) in self.p_set:
            if self.DEBUG:
                print("New point already exist!")
            self.add_rand_point(min_max_val, precision)
        else:
            if self.DEBUG:
                print("New point is unique!")
            self.add_point(tuple(point))

    def add_n_rand_point(self, n, min_max_val, precision):
        """add n amount of randomized points to p_set

        :param n: amount of points to be added
        :param min_max_val: determines the minimum and maximum value for randomization
        :param precision: determines digit count of fractional part
        """
        for i in range(n):
            self.add_rand_point(min_max_val, precision)

    def get_point(self, index):
        """get point from p_set at index=index

        :param index: point index in set
        :return: return point (tuple of numbers) at index=index
        """
        return self.p_set[index]

    def get_set(self):
        """get p_set

        :return: instance's p_set
        """
        return self.p_set

    def get_info_string(self):
        """get information about PointSet instance

        :return: string of PointSet information
        """
        info = ""
        info += "Dimension : " + str(self.p_dimension) + "\n"
        info += "Number of Points : " + str(self.p_count) + "\n"
        info += "Points :\n"
        for points in self.p_set:
            info += " " + str(points) + "\n"
        return info

    def print_info(self):
        """prints information of PointSet instance"""
        info = self.get_info_string()
        print(info)

    # SOLVER
    def nearest_pair_bf(self):
        """get nearest pair from point set using brute force

        :return: nearest_point and recorded processing time
        """
        start_time = time.time()
        min_dist = float('inf')
        nearest_pair = None
        op_count = 0

        for i in range(self.p_count - 1):
            for j in range(i + 1, self.p_count):
                curr_dist = PointSet.euclid_distance(self.get_point(i), self.get_point(j))
                op_count += 1
                if curr_dist < min_dist:
                    min_dist = curr_dist
                    nearest_pair = (self.get_point(i), self.get_point(j))
        recorded_time = time.time() - start_time

        return nearest_pair, min_dist, recorded_time, op_count

    @staticmethod
    def euclid_distance(point1, point2):
        """calculate euclidean distance between two points

        :param point1: tuple of numbers
        :param point2: tuple of numbers
        :return: euclidean distance of both points
        """
        return math.sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))
