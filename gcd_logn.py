import sys

# Find GCD in Log N
# INPUT:-
# 2 numbers a&b
# 5 15
# OUTPUT:-
# 5

a,b=map(int,input().split())
def gcd(a,b):   
    # using Euclidean algorithm
    # Time Complexity O(log(min(a,b)))
    if (a == 0): 
        return b 
    if (b == 0): 
        return a 
    if (a == b): 
        return a  
    if (a > b): 
        return gcd(a-b, b) 
    return gcd(a, b-a)
