# This problem was asked by Stripe.
# Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
# You can modify the input array in-place.

# Solutions 
#1) First solution I came up with was sorting the list O(nlogn), and then just going through the list until a missing integer is found. However the issue with this is that it takes O(nlogn) time
#2) The next solution was to get ride of the sorting run time issue by using a hash map.  That is, create a hash map of all positive integers in list in O(n) time, and then go through al positive integers starting at 1 and check if it exists in the hash map.  However this is in O(n) time it requires O(n) extra memory
#3) The thrid solution I had to search online for regretably, it was to use swapping to seperate the negative/zero values from the rest in O(n) time.  Then since we know that all the right side positive integers (in unsorted form) have to being properly increamenting from 1 to N (size of array right side), so each positive integer though unsorted must correspond to an index value.  That is: if list is [3, 4, -1 , 1], which becomes [-1, 4, 3, 1], then [4, 3, 1] right list must correspond to an index [0, 1, 2]. As index starts from zero if we add one [1, 2, 3], so if we try to map the positive integer values to an index we can see if such an index positive number exists in the right list, if not than its missing.

#list = [3, 4, -1, 1] # Missing 2
#list = [7, -2, 0, 0, 1, 4, 6, 7, 3, 10, -10, -4] # Missing 2
#list = [1, 2, 3, 4, 6, 7, 8, 9] # Missing 5
list = [15, -5, 0, 8, -9, 5, 1, 4, 2, 12] # Missing 3

def swap(index1, index2):
    tmp = list[index1]
    list[index1] = list[index2]
    list[index2] = tmp

def split():
    firstPos = 0
    for i in range(len(list)):
        val = list[i]
        if 0 >= val:
            swap(firstPos, i) # swap positive and negative
            firstPos += 1
    return firstPos

def findFirstPos():
    # Seperate negative and zero from positive integers
    firstPos = split()
    print "Split List: ", list
    print "First Pos: ", firstPos

    # Go through list and mark index's where an appropriate list value exists in list
    size = len(list) - firstPos
    for i in range(size):
        index = i + firstPos
        if abs(list[index]) - 1 + firstPos < size:
            list[abs(list[index]) - 1 + firstPos] *= -1 # mark as visited
    
    # Search to find missig positive integer
    max = 1    
    for i in range(size):
        index = i + firstPos
        if list[index] > max:
            max = list[index]
        
        if list[index] > 0:
            return i + 1
    
    return max

val = findFirstPos()
print "Missing: ", val