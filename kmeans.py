class KdTree:
    def __init__(self, root):
        self.root = root
        self.k = len(root.points)

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


points = [[2,3], [1,1], [6,3], [4,5]]

tree = KdTree(KNode([4,3]))

for point in points:
    tree.insert(point)

print(tree.search([2,3]))
