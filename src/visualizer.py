import matplotlib
from matplotlib import pyplot as plt
from point_set import *
def visualizer(p_dimension, p_set, pair_dnc):
    fig = plt.figure(figsize=(150,150))

    if p_dimension==3:
        ax = fig.add_subplot(111, projection="3d")
        for i in range(len(p_set)):
            ax.scatter(p_set[i][0],p_set[i][1],p_set[i][2],c='b',marker='o')
        for i in range(0,len(pair_dnc)):
            for j in range(0, len(pair_dnc[i])):
               ax.scatter(pair_dnc[i][j][0],pair_dnc[i][j][1],pair_dnc[i][j][2],c='r',marker='o')
        x1 = [pair_dnc[0][0][0], pair_dnc[0][1][0]]
        x2 = [pair_dnc[0][0][1], pair_dnc[0][1][1]]
        x3 = [pair_dnc[0][0][2], pair_dnc[0][1][2]]
        plt.plot(x1,x2,x3 , 'ro-') 

    if p_dimension==2:
        for i in range(len(p_set)):
            plt.scatter(p_set[i][0],p_set[i][1],color = 'b')
        for i in range(len(pair_dnc)):
            for j in range(0, len(pair_dnc[i])):
                plt.scatter(pair_dnc[i][j][0],pair_dnc[i][j][1],color = 'r')
        #draw line
        x1 = [pair_dnc[0][0][0], pair_dnc[0][1][0]]
        x2 = [pair_dnc[0][0][1], pair_dnc[0][1][1]]
        plt.plot(x1,x2 , 'ro-') 

        x = []
        y = []
        for i in range(len(p_set)):
            x.append(p_set[i][0])
            y.append(p_set[i][1])
        for xy in zip(x,y):
            plt.annotate('(%.2f,%.2f)'% xy, xy = xy)
        
    plt.show()