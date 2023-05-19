class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def invertir_arbol(root):
    if root is None:
        return None

    invertir_arbol(root.left)
    invertir_arbol(root.right)

    temp = root.left
    root.left = root.right
    root.right = temp

    return root


def in_order(node):
    if node:
        in_order(node.left)
        print(node.value)
        in_order(node.right)

'''
Tree : Inorder
                      1
                      |
            ----------------------
            |                     | 
            2                     3  
            |                     | 
       ----------            ------------          
       |        |            |          |
       4        5            6          7
       
  -> 4 2 5 1 6 3 7
'''

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("--Árbol In Order--")
in_order(root)
root = invertir_arbol(root)
print("--Árbol Invertido--")
in_order(root)
