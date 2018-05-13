# This problem was asked by Facebook.
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.
msg = '114215'

def decodeCount(msg, index = 0):
    if "" == msg or "0" in msg:
        return 0
        
    # Check if at last index of permutation
    if index >= len(msg):
        return 1
        
    # Including Current index
    # Go to next index - jump by +1
    count = decodeCount(msg, index + 1)

    # Including Pair Index
    # Go to next after pair - jump +2
    pair = msg[index: index + 2]
    if len(msg) - index >= 2 and int(pair) <= 26:
        count += decodeCount(msg, index + 2)

    return count

print decodeCount(msg)