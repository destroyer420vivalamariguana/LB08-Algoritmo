'''
Created on Mar 11, 2019
@author: jgomezm
@version: 1.2 April 29,2020
'''
class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right  # right child
# In-order recursive traversal. The
# nodes' values are appended to the
# result list in traversal order


def inOrderRecursive(root, result):
    if not root:
        return
    inOrderRecursive(root.left, result)
    result.append(root.data)
    inOrderRecursive(root.right, result)


'''
Binary Tree : Inorder Traversal

                      1
                      |
            ----------------------
            |                     | 
            2                     3  
            |                     | 
       ----------            ------------          
       |        |            |          |
       4        5            6          7

     --> 4 2 5 1 6 3 7 
'''
childrenLeftLeft = BinaryTreeNode(4)
childrenLeftRight = BinaryTreeNode(5)
childrenRightLeft = BinaryTreeNode(6)
childrenRightRight = BinaryTreeNode(7)
childrenLeft = BinaryTreeNode(2, childrenLeftLeft, childrenLeftRight)
childrenRight = BinaryTreeNode(3, childrenRightLeft, childrenRightRight)
root = BinaryTreeNode(1, childrenLeft, childrenRight)
result = []
inOrderRecursive(root, result)
print(result)