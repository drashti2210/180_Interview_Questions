import sys

# Count Trailing zero in n!
# INPUT:-
# n
# 1
# 5
# OUTPUT: -
# 1

n=int(input())
# solution 
# checking multiplication of 5 as 1st trailing zero occurs at 5!
# Time complexity O(logn-base 5)

def Trailing_Count(n):
    ans = 0
    while n > 0:
        n //= 5
        ans += n
    return(ans)