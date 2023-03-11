# demotools
# author: Trae Claar

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# creates a Poly3DCollection from a matrix and returns it
def create_poly(matrix):
    
    # make a list of column vectors
    columns = []
    for i in range(len(matrix[0])):
        columns.append(matrix[:,i])

    # calculate vertices of faces
    vertices = []
    n = len(columns)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                vertices.append([columns[i], columns[j], columns[k]])

    # create and return polygon
    return Poly3DCollection(vertices)

# display objects, each defined by a provided matrix
# useful if the object(s) is no longer needed after being displayed
def display_objects(*matrices):

    # matplotlib setup stuff
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # create a Poly3DCollection for each object and add it to the plot
    # also find the largest and smallest values in the matrices for later use
    minVal = np.amax(matrices[0])
    maxVal = np.amin(matrices[0])
    for matrix in matrices:
        poly = create_poly(matrix)
        ax.add_collection3d(poly)

        minVal = min(minVal, np.amin(matrix))
        maxVal = max(minVal, np.amax(matrix))

    # determine values used for diagram limits
    size = abs(maxVal - minVal)
    mid = (maxVal + minVal) / 2
    lim1 = mid - size
    lim2 = mid + size

    # set the limits of the plot diagram
    ax.set_xlim(lim1, lim2)
    ax.set_ylim(lim1, lim2)
    ax.set_zlim(lim1, lim2)

    zeros = np.linspace(0, 0, 50)
    axis = np.linspace(lim1 - 10, lim2 + 10, 50)
    ax.plot3D(zeros, zeros, axis, 'red') # z axis
    ax.plot3D(zeros, axis, zeros, 'red') # y axis
    ax.plot3D(axis, zeros, zeros, 'red') # x axis

    # show the plot
    plt.show()

    

    
    
