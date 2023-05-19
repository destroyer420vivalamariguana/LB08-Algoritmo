class TreeNode:

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def LongWay(root):
    if not root:
        return []

    def preOrder(node, currentpath, longway):
        if not node:
            return
        currentpath.append(node.data)
        if not node.left and not node.right:
            if len(currentpath) > len(longway):
                longway.clear()
                longway.extend(currentpath)

        preOrder(node.left, currentpath, longway)
        preOrder(node.right, currentpath, longway)

        currentpath.pop()

    currentpath = []
    longway = []
    preOrder(root, currentpath, longway)

    return longway

'''
Tree 

                      1
                      |
            ----------------------
            |                     | 
            2                     3  
            |                     | 
       ------------          --------------          
       |          |          |             |
       8          9          4             5
    ---------
    |       |
    6       10
       
'''
childrenLeftLeftRight = TreeNode(10)
childrenLeftLeftLeft = TreeNode(6)
childrenLeftLeft = TreeNode(8, childrenLeftLeftLeft,childrenLeftLeftRight)
childrenLeftRight = TreeNode(9)
childrenRightLeft = TreeNode(4)
childrenRightRight = TreeNode(5)
childrenLeft = TreeNode(2, childrenLeftLeft, childrenLeftRight)
childrenRight = TreeNode(3, childrenRightLeft, childrenRightRight)
root = TreeNode(1, childrenLeft, childrenRight)

camino_largo = LongWay(root)
print(camino_largo)