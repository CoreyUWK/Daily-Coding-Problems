#This problem was asked by Google.
#Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize_inner(node, serial):
    if None == node:
        return serial
        
    serial += "Node('" + node.val + "'"
    if (None != node.left):
        serial = serialize_inner(node.left, serial + ", ")
    if (None != node.right):
        serial = serialize_inner(node.right, serial + ", ")
    
    return serial + ")"
            
def serialize(node):
    return serialize_inner(node, "")

def deserialize(str):
    return eval(str)

#The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
print(serialize(node))
print serialize(deserialize(serialize(node)))
print( deserialize(serialize(node)).left.left.val)
assert deserialize(serialize(node)).left.left.val == 'left.left'

# Output:
# Node('root', Node('left', Node('left.left')), Node('right'))
# left.left
