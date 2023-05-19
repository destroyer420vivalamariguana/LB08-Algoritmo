class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def findMaxRecursive(tree):
    if tree is None:
        return float("-inf")

    data = tree.data
    left_max = findMaxRecursive(tree.left)
    right_max = findMaxRecursive(tree.right)

    return max([data, left_max, right_max])


def findMinRecursive(tree):
    if tree is None:
        return float("inf")

    data = tree.data
    left_min = findMinRecursive(tree.left)
    right_min = findMinRecursive(tree.right)

    return min([data, left_min, right_min])

'''
Binary Tree

                      1
                      |
            ----------------------
            |                     |
            2                     3
            |                     |
       ----------            ------------
       |        |            |          |
       4        7            8          5
'''
childrenLeftLeft = BinaryTreeNode(4)
childrenLeftRight = BinaryTreeNode(7)
childrenRightLeft = BinaryTreeNode(8)
childrenRightRight = BinaryTreeNode(5)
childrenLeft = BinaryTreeNode(2, childrenLeftLeft, childrenLeftRight)
childrenRight = BinaryTreeNode(3, childrenRightLeft, childrenRightRight)
root= BinaryTreeNode(1, childrenLeft, childrenRight)
maxData =findMaxRecursive(root)
minData = findMinRecursive(root)
print("Num Max:",maxData)
print("Num Min",minData)