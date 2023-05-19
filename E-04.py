class BinaryTreeNode:

    def __init__(self, data, left = None, right = None):
        self.data = data  # value node
        self.left = left  # left child
        self.right = right  # right child

def sumRecursive(root):
    if (root == None):
        return 0
    return root.data + \
        sumRecursive(root.left) + \
        sumRecursive(root.right)


def sumPares(root): #Suma de numeros pares
    if (root == None):
        return 0

    suma = 0
    if root.data % 2 == 0:
        suma += root.data

    if root.left != None:
        suma += sumPares(root.left)
    if root.right != None:
        suma += sumPares(root.right)

    return suma

#
# Resolution
#           1
#       2       3
#     7   5   6   7

root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.left.left = BinaryTreeNode(7)
root.left.right = BinaryTreeNode(5)
root.right.left = BinaryTreeNode(6)
root.right.right = BinaryTreeNode(7)

sumap= sumPares(root)
print("La suma de los numeros pares arbol es %d" % (sumap))
