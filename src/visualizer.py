"""
:file: visualizer.py

visualize points and solution from the closest pair problem (2D/3D)
"""

from matplotlib import pyplot as plt
from point_set import *


def visualizer(p_dimension, p_set, pair_dnc):
    """visualize points and solution

    :param p_dimension: dimension of points
    :param p_set: set of points
    :param pair_dnc: solution of the closest pair problem (divide and conquer)
    """
    fig = plt.figure(figsize=(100, 100))

    if p_dimension == 3:
        ax = fig.add_subplot(111, projection="3d")
        for i in range(len(p_set)):
            ax.scatter(p_set[i][0], p_set[i][1], p_set[i][2], c='b', alpha=0.5, marker='o')
        for i in range(0, len(pair_dnc)):
            for j in range(0, len(pair_dnc[i])):
                ax.scatter(pair_dnc[i][j][0], pair_dnc[i][j][1], pair_dnc[i][j][2], c='r', marker='o')

        for i in range(0, len(pair_dnc)):
            x1 = [pair_dnc[i][0][0], pair_dnc[i][1][0]]
            x2 = [pair_dnc[i][0][1], pair_dnc[i][1][1]]
            x3 = [pair_dnc[i][0][2], pair_dnc[i][1][2]]
            plt.plot(x1, x2, x3, 'ro-')

    if p_dimension == 2:
        for i in range(len(p_set)):
            plt.scatter(p_set[i][0], p_set[i][1], alpha=0.5, color='b')
        for i in range(len(pair_dnc)):
            for j in range(0, len(pair_dnc[i])):
                plt.scatter(pair_dnc[i][j][0], pair_dnc[i][j][1], color='r')

        # draw line
        for i in range(0, len(pair_dnc)):
            x1 = [pair_dnc[i][0][0], pair_dnc[i][1][0]]
            x2 = [pair_dnc[i][0][1], pair_dnc[i][1][1]]
            plt.plot(x1, x2, 'ro-')

        x = []
        y = []
        for i in range(len(p_set)):
            x.append(p_set[i][0])
            y.append(p_set[i][1])

    plt.show()
