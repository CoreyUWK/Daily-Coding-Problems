#This problem was asked by Google.
#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
#For example, given the following Node class
#class Node:
#    def __init__(self, val, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right
#The following test should pass:
#node = Node('root', Node('left', Node('left.left')), Node('right'))
#assert deserialize(serialize(node)).left.left.val == 'left.left'

def serialize(node):
    if None == node:
        return node
    str = ""
    str += "Node('" + node.val + "'"
    left = serialize(node.left)
    right = serialize(node.right)
    if None != left: str += ", " + left
    if None != right: str += ", " + right
    str += ")"
    return str

def deserialize(str):
    return eval(str)

print(serialize(node))
print( deserialize(serialize(node)).left.left.val)
# Output:
# Node('root', Node('left', Node('left.left')), Node('right'))
# left.left