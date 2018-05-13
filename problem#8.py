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


def numUnival(root, count=0):
    if None == root:
        return count
    
    val = root.val
   
    if (None == root.left and None == root.right):
        count += 1
    elif (val == root.left.val and val == root.right.val):
        print "Val: ", val
        print " Left: ", root.left.val
        print " Right: ", root.right.val
        count += 1

    count = numUnival(root.left, count)
    count = numUnival(root.right, count)
    
    return count
    

#root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))) # => 5
#root = Node(0, Node(0, Node(0), Node(0)), Node(0, Node(0), Node(0))) # => 7
#root = Node(0, Node(1, Node(0), Node(0)), Node(1, Node(0), Node(0))) # => 4
root = Node(0, Node(0), Node(0, Node(0), Node(0, Node(None), Node(1))))
printTree(root)
print numUnival(root)
