#Today’s problem is taken from the “Daily Coding Problem” https://www.dailycodingproblem.com/
#This problem was asked by Uber.
#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can’t use division?

# Bryce Solution using division
from operator import mul
from functools import reduce
def prob(lis):
    prod = reduce(mul, lis)
    return [ prod // v for v in lis ]

# Solution without division
def prob2(lis):
    ret = [1] * len(lis)
    fwd = 1
    rev = 1

    for i in range(len(lis)):
        j = -(i+1)
        ret[i] *= fwd
        ret[j] *= rev
        print(i, ret)
        fwd *= lis[i]
        rev *= lis[j]

    return ret
    
    
# My Solution using division
