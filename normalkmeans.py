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
    minima = [sys.maxsize for i in range(k)];
    maxima = [-sys.maxsize - 1 for i in range(k)];

    for point in points:
        for f in range(len(point)):
            if (point[f] < minima[f]):
                minima[f] = point[f];

            if (point[f] > maxima[f]):
                maxima[f] = point[f];

    Z = [[0 for j in range(k)] for i in range(k)]

    for i in range(k):
        for j in range(k):
            center = random.randint(minima[j], maxima[j])
            Z[i][j] = center

    return Z

def euclideanDistance(pointA, pointB):
    sums = 0
    for i in range(len(pointA)):
        sums += pow((pointA[i]-pointB[i]),2)

    return math.sqrt(sums)

def reCalculateMeans(centroids, clusters):
    i = 0
    for cluster in clusters:
        avg = [float(sum(col))/len(col) for col in zip(*cluster)]
        print(avg)
        centroids[i] = avg
        i += 1
    print("Centroides nuevos", centroids)

def kmeans(points, centroids):
    for point in points:
        minPoint = euclideanDistance(point, centroids[0])
        index = 0
        print("Punto: ",point)
        for centroid in centroids:
            print("Centroide: ", centroid)
            print("Distancia: ", euclideanDistance(point, centroid))
            min = euclideanDistance(point, centroid)
            if min < minPoint:
                minPoint = min
                index = centroids.index(centroid)
        print("Distancia minima",minPoint)
        print(index)
        clusters[index].append(point)
        print("\n")
    print(clusters)
    print("Centroides viejos", centroids)
    reCalculateMeans(centroids, clusters)
    print(clusters)

points = read()
k = len(points[0])

centroids = generateKCenters(k)
clusters = [[] for x in range(k)]
kmeans(points, centroids)



