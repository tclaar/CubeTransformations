# demotools
# author: Trae Claar

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

AXIS_UPPER_LIMIT = 20
AXIS_LOWER_LIMIT = -20

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
    for matrix in matrices:
        poly = create_poly(matrix)
        ax.add_collection3d(poly)

    # set the limits of the plot diagram
    ax.set_xlim(AXIS_LOWER_LIMIT, AXIS_UPPER_LIMIT)
    ax.set_ylim(AXIS_LOWER_LIMIT, AXIS_UPPER_LIMIT)
    ax.set_zlim(AXIS_LOWER_LIMIT, AXIS_UPPER_LIMIT)

    zeros = np.linspace(0, 0, 2)
    axis = np.linspace(AXIS_LOWER_LIMIT * 1.5, AXIS_UPPER_LIMIT * 1.5, 2)
    ax.plot3D(axis, zeros, zeros, 'green') # x axis
    ax.plot3D(zeros, axis, zeros, 'purple') # y axis
    ax.plot3D(zeros, zeros, axis, 'red') # z axis
    
    # show the plot
    plt.show()
