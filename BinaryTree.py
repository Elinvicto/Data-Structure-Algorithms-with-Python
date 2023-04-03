class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def getLeafCount(node):
    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return getLeafCount(node.left)