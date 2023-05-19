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

def sumLeftNodo(root): #Suma de los nodos izquierdos
    if(root == None):
        return 0
    return sumRecursive(root.left)


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

sumaLN= sumLeftNodo(root)
print("Suma de elementos del nodo izquierdo del arbol es %d" % (sumaLN))