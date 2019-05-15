import sys
import math
import random

def read():

    it = iter(sys.stdin.read().splitlines())

    n, k = [int(x) for x in next(it).split(" ")]

    points = []

    for i in range(n):
        points.append([int(x) for x in next(it).split(" ")])

    return points

def generateKCenters(k):
    minima = [sys.maxsize-1 for i in range(k)];
    maxima = [-sys.maxsize +1 for i in range(k)];

    for point in points:
        for f in range(len(point)):
            if (point[f] < minima[f]):
                minima[f] = point[f]

            if (point[f] > maxima[f]):
                maxima[f] = point[f]

    Z = [[0 for j in range(k)] for i in range(k)]

    for i in range(k):
        for j in range(k):
            center = random.randint(minima[j], maxima[j])
            Z[i][j] = center
    return Z

def euclideanDistance(pointA, pointB):
    sums = 0
    for i in range(k):
        sums += ((pointA[i]-pointB[i]))**2
    return math.sqrt(sums)

def reCalculateMeans(centroids, clusters):
    averages = []
    for cluster in clusters:
        avg = [float(sum(col))/len(col) for col in zip(*cluster)]
        if len(avg) > 0:
            averages.append(avg)
        else:
            averages.append([0 for x in range(k)])
    for i in range(len(centroids)):
        if len(averages) > 1:
            centroids[i] = averages[i]
def kmeans(points, centroids,clusters,  N):
    i = 0
    while i < N:
        for point in points:
            minPoint = euclideanDistance(point, centroids[0])
            index = 0
            for j  in range(len(centroids)):
                min = euclideanDistance(point, centroids[j])
                if min < minPoint:
                    minPoint = min
                    index = centroids.index(centroids[j])
            clusters[index].append(point)

        reCalculateMeans(centroids, clusters)
        final = clusters[::1]
        clusters = [[] for x in range(k)]
        i += 1
    print("Procedimiento completado con", i, "iteracion(es)")
    j = 1
    for cluster in final:
        print("Cluster",j,":", cluster)
        j+= 1


points = read()
k = len(points[0])

centroids = generateKCenters(k)
clusters = [[] for x in range(k)]
kmeans(points, centroids, clusters, 60)



