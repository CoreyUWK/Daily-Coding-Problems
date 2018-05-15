# *********************************************
# For problem 8, using same Node class as problem 3
# Returns a tuple (unisub_count, node_count)
def unisub_rec(node):
    if node == None:
        return (0,0)
    
    left = unisub_rec(node.left)
    right = unisub_rec(node.right)

    # If the unisub_count is equal to the number of nodes, then the whole
    # subtree is a unival subtree.
    left_is_unival = left[0] == left[1]
    right_is_unival = right[0] == right[1]
    
    same_child_vals = ((node.left == None or node.left.val == node.val) and
                       (node.right == None or node.right.val == node.val))

    node_is_unival = same_child_vals and left_is_unival and right_is_unival

    return (left[0] + right[0] + (1 if node_is_unival else 0),
            left[1] + right[1] + 1)

def unisub_count(node):
    return unisub_rec(node)[0]

## Example has 5 unival subtrees:
eg = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
print("unival count:", unisub_count(eg))

# *********************************************
# Simplistic answer for the coin counting problem. Basically brute force + memoization
def makechange(coins, value, mem):
    if value < min(coins):
        return 0
    if value in mem:
        return mem[value]

    ret = None
    for coin in coins:
        subcount = makechange(coins, value - coin, mem) 
        if ret == None or subcount > 0 and subcount < ret:
            ret = subcount

    mem[value] = 1 + ret
    return 1 + ret 
    

coins = set([1,7,10])
value = 15
mem = {c:1 for c in coins}
print(makechange(coins, value, mem))


# *********************************************
# My answer for problem 7. Assumed we only need to count possibilities, not print the decoded strings.
def encodings_rec(string, r):
    if r == len(string):
        return 1
    if string[r] == "0":
        return 0
    count = encodings_rec(string, r + 1)
    if len(string) - r >= 2 and int(string[r:r+2]) < 26:
        count += encodings_rec(string, r + 2)
    return count

def encodings(string):
    return encodings_rec(string, 0)

print(encodings("111"))

# *********************************************
# Solution for problem 3:
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