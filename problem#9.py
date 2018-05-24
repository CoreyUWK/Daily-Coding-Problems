# This problem was asked by Airbnb.
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 8] should return 12, since we pick 4 and 8. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Follow-up: Can you do this in O(N) time and constant space?
#list=[2, 4, 6, 8] # => 12
#list = [2,3,4,5] # => 8
#list = [5,5,10,-40,1,-4,40,50,35] => 91
list = [4,-5,3,4,-1,5,6]

def findMaxSumNoOptimal(list):
    # sort O(nlogn) => now in sorted tuple of (value, index)
    # reverse loop add values to addlist if index not +/-1 from any other in addList and increases sum
    # return sum

def findMaxSum(list):
    incl = 0
    excl = 0

    print "i : excl", "incl"
    for i in range(len(list)):
        # for next iteration incl should be excl + item if greater
        new_incl = max(excl + list[i], excl)
        new_excl = max(excl, incl) # Update to max of previous 2
        
        # Update (seperate so better to follow and prevents using incorrect new value)
        excl = new_excl
        incl = new_incl
        
        print i, ":", excl, incl
    
    return incl
        
print list
val = findMaxSum(list)
print "Max: ", val