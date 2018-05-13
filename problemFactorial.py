def factorialLoop(val):
    if 0 >= val:
        return val
    
    res = 1
    for i in range(val, 0, -1):
        res *= i
    return res
    
def factorialRecursive(val):
    if 1 >= val:
        return val
    return val * factorialRecursive(val - 1)
    
print factorialRecursive(4)