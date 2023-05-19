class BinaryTreeNode:

    def __init__(self, data, left=None, right=None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right  # right child

def postOrderRecursive(root, result):
    if not root:
        return

    postOrderRecursive(root.left, result)
    postOrderRecursive(root.right, result)
    result.append(root.data)

'''
Binary Tree : Postorder Traversal

                      1
                      |
            ----------------------
            |                     | 
            2                     3  
            |                     | 
       ----------            ------------          
       |        |            |          |
       4        5            6          7

     --> 4 5 2 6 7 3 1
'''
childrenLeftLeft = BinaryTreeNode(4)
childrenLeftRight = BinaryTreeNode(5)
childrenRightLeft = BinaryTreeNode(6)
childrenRightRight = BinaryTreeNode(7)
childrenLeft = BinaryTreeNode(2, childrenLeftLeft, childrenLeftRight)
childrenRight = BinaryTreeNode(3, childrenRightLeft, childrenRightRight)
root = BinaryTreeNode(1, childrenLeft, childrenRight)
result = []
postOrderRecursive(root, result)
print(result)