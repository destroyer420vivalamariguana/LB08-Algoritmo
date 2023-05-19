class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right  # right child

def preOrderRecursive(root, result):
    if not root:
        return

    result.append(root.data)
    preOrderRecursive(root.left, result)
    preOrderRecursive(root.right, result)


'''
Binary Tree : Preorder Traversal

                      1
                      |
            ----------------------
            |                     | 
            2                     3  
            |                     | 
       ----------            ------------          
       |        |            |          |
       4        5            6          7

     --> 1 2 4 5 3 6 7
'''
childrenLeftLeft = BinaryTreeNode(4)
childrenLeftRight = BinaryTreeNode(5)
childrenRightLeft = BinaryTreeNode(6)
childrenRightRight = BinaryTreeNode(7)
childrenLeft = BinaryTreeNode(2, childrenLeftLeft, childrenLeftRight)
childrenRight = BinaryTreeNode(3, childrenRightLeft, childrenRightRight)
root = BinaryTreeNode(1, childrenLeft, childrenRight)
result = []
preOrderRecursive(root, result)
print(result)
