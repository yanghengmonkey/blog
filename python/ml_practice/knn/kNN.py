from numpy import *
import operator

def createDataSet():
    group = array([
                   [1.0,1.1],
                   [1.0,1.0],
                   [0.0,0.0],
                   [0.0,0.1]
                  ])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    # Get distances
    dataSetSize = dataSet.shape[0]
    distances = (((tile(inX, (dataSetSize, 1)) - dataSet)**2).sum(axis=1))**0.5
    # Sort
    class_counts = {}
    sorted_distances = distances.argsort()
    for index in range(k):
        class_counts[ labels[sorted_distances[index]] ] = class_counts.get( labels[sorted_distances[index]], 0) + 1
    sorted_class_counts = sorted( class_counts.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_class_counts[0][0]


