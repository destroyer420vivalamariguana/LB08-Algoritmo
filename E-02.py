'''
Created on Mar 11, 2019
@author: jgomezm
@version: 1.2    April 29,2020
'''
class BinaryTreeNode:

    def __init__(self, data, left = None, right = None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right # right child


def findMaxRecursive(tree):
    # Base case
    if tree is None:
        return float('-inf')  # Mininum value

    data = tree.data
    left_max = findMaxRecursive(tree.left)
    right_max = findMaxRecursive(tree.right)

    return max([data, left_max, right_max])


'''
Binary Tree

                      1
                      |
            ----------------------
            |                     | 
            2                     3  

'''

childrenLeft = BinaryTreeNode(2)
childrenRight = BinaryTreeNode(3)
root = BinaryTreeNode(1, childrenLeft, childrenRight)

maxData = findMaxRecursive(root)
print("Num Max:",maxData)
