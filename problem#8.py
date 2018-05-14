# This problem was asked by Google.
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(root, level = 0, side = "top", parent = "None"):
    if None != root:
        print "level:", str(level), "parent: ", parent, "side:", side, "Val:", str(root.val)
    
    if None != root.left:
        printTree(root.left, level + 1, "left", str(root.val))
    
    if None != root.right:
        printTree(root.right, level + 1, "right", str(root.val))

def isUnival(node, val):
    if None == node:
        return False
    
    if None == node.left and None == node.right:
        return True
    elif None == node.left:
        return False
    elif None == node.right:
        return False
    
    equalChildren = (val == node.left.val) and (val == node.right.val) 
    return True if equalChildren and isUnival(node.left, val) and isUnival(node.right, val) else False
    

def numUnival(root):
    if None == root:
        return 0

    countLeft = numUnival(root.left)
    countRight = numUnival(root.right)
    
    return 1 + countLeft + countRight if isUnival(root, root.val) else countLeft + countRight 
    

#root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))) # => 5
#root = Node(0, Node(0, Node(0), Node(0)), Node(0, Node(0), Node(0))) # => 7
#root = Node(0, Node(1, Node(0), Node(0)), Node(1, Node(0), Node(0))) # => 4
#root = Node(0, Node(0), Node(0, Node(0), Node(0, None, Node(1))))
root = Node(0)
root.left = Node(0)
root.right = Node(0)
root.right.left = Node(0)
root.right.right = Node(0)
root.right.right.left = None
root.right.right.right = Node(1)

printTree(root)
print numUnival(root)
