import sys

#Day 3
#4. Find GCD in Log N
# INPUT:-
# 2 numbers a&b
# 1
# 5 15
# OUTPUT:-
# 5

#input output files
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

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

for t in range(int(input())):
    a,b=map(int,input().split())
    print(gcd(a,b))