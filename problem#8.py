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
    if root is not None:
        print "level:", str(level), "parent: ", parent, "side:", side, "Val:", str(root.val)
    
    if root.left is not None:
        printTree(root.left, level + 1, "left", str(root.val))
    
    if root.right is not None:
        printTree(root.right, level + 1, "right", str(root.val))

def numUnival_inner(root):
    if root is None:
        return 0, True
    
    countLeft, isLeftUnival = numUnival_inner(root.left)
    countRight, isRightUnival = numUnival_inner(root.right)
    total = countLeft + countRight
    
    if isLeftUnival and isRightUnival:
        if root.left is not None and root.left.val != root.val:
            return total, False
        elif root.right is not None and root.right.val != root.val:
            return total, False
        else:
            return total + 1, True
    else:
        return total, False
    

def numUnival(root):
    count, _ = numUnival_inner(root)
    return count


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
