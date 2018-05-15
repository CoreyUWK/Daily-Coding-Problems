# This problem was asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?
#list=[2, 4, 6, 8]
list=[5, 1, 1, 5]

def largestNonAdjacentSum(list):
    newList = []
    for i in range(len(list)):
        newList.append(tuple([list[i], i]))
    newList = sorted(newList)

    key = 1
    value = 0
    for a in newList:
        print "Key:", a[key], "Value:", a[value]
        
    if newList[-2][key] + 1 == newList[-1][key]:
        return newList[-1][value] + newList[-3][value]
    return newList[-1][value] + newList[-2][value]
    
print largestNonAdjacentSum(list)