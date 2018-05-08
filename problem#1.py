# Given a list of numbers, return whether any two sums to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?
list = [11, 3, 10, 7, 18, 9, 12, 14, 1, 2, 3, 88, 100, 101, 103, 115]
k = 218

def isSum(sum, list):
    dict = {val: 1 for val in list}   # O(n)
    listDiff = [(sum - val) for val in list]   # O(n)

    print "Dict: ", dict 
    print "ListDiff: ", listDiff 
    
    for v in listDiff:   # O(n)
        if 1 == dict.get(v): 
            print v, " + ", sum - v, " = ", sum
            return True
    return False
    
print "Result: \n", isSum(k, list)