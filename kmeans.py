class KdTree:
    def __init__(self, points):
        self.k = len(points[0])
        self.root = self.buildTree(points,0)

    def buildTree(self,points, depth):
        cd = depth % self.k
        pointsOrdered = sorted(points, key=lambda x: x[cd])
        mid = len(pointsOrdered)//2
        node = KNode(pointsOrdered[mid])

        print(points)
        node.left = self.buildTree(pointsOrdered[:mid:], depth+1) if len(pointsOrdered[:mid:]) > 1 else None
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
    def __init__(self, points):
        self.points = points
        self.left = None
        self.right = None
