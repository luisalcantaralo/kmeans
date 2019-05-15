import sys
import random

class KdTree:
    def __init__(self, points):
        self.k = len(points[0])
        self.root = self.buildTree(points,0)

    def buildTree(self,points, depth):

        cd = depth % self.k
        pointsOrdered = sorted(points, key=lambda x: x[cd])
        mid = len(pointsOrdered)//2

        wgtCent = 0
        for point in pointsOrdered:
            wgtCent += point[cd]

        node = KNode(pointsOrdered[mid],len(pointsOrdered), wgtCent, pointsOrdered[mid][cd])


        node.left = self.buildTree(pointsOrdered[:mid:], depth+1) if len(pointsOrdered[:mid:]) > 0 else None
        node.right = self.buildTree(pointsOrdered[mid+1::],depth+1) if len(pointsOrdered[mid::]) > 1 else None

        return node

    def insertNode(self, node, point, depth):
        dimension = depth % self.k
        if point[dimension] < node.points[dimension]:
            if node.left == None:
                newNode = KNode(point)
                node.left = newNode
            else:
                self.insertNode(node.left, point, depth+1)
        else:
            if node.right == None:
                newNode = KNode(point)
                node.right = newNode
            else:
                self.insertNode(node.right, point, depth+1)


    def insert(self, point):
        return self.insertNode(self.root, point, 0)

    def searchNode(self, node, point, depth):

        if node == None:
            return False
        if node.points == point:
            return True
        dimension = depth % self.k
        if point[dimension] < node.points[dimension]:
            return self.searchNode(node.left, point, depth+1)

        return self.searchNode(node.right, point, depth+1)


    def search(self, point):
        return self.searchNode(self.root, point, 0)



class KNode:
    def __init__(self, points, count, wgtCent, axis):
        self.points = points
        self.left = None
        self.right = None
        self.centroid = wgtCent/count
        self.axis = axis
        # Compute number of associated data u.count and weighted centroid

        # u.wgtCente vector sum of associated points



    def isLeaf(self):
        return points.count == 1


def generateKCenters(k):
    # Random K Centers
    minima = [sys.maxsize for i in range(tree.k)];
    maxima = [-sys.maxsize - 1 for i in range(tree.k)];

    for point in points:
        for f in range(len(point)):
            if (point[f] < minima[f]):
                minima[f] = point[f];

            if (point[f] > maxima[f]):
                maxima[f] = point[f];

    Z = [[0 for j in range(tree.k)] for i in range(tree.k)]

    for i in range(tree.k):
        for j in range(tree.k):
            center = random.randint(minima[j], maxima[j])
            Z[i][j] = center

    return Z


# Points
points = [(2,3,2), (1,1,3), (6,3,8), (4,5,2), (7,8,5), (2,5,0)]
tree = KdTree(points)



