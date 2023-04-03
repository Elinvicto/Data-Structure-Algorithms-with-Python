class newNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def getLeafCount(root):
    if (root == None or (root.left == None and root.right == None)):
        return 0