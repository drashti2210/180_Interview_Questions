import sys

#Day 3
#3. Count Trailing zero in n!
# INPUT:-
# n
# 1
# 5
# OUTPUT: -
# 1

#input output files
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

for t in range(int(input())):
    # solution 
    # checking multiplication of 5 as 1st trailing zero occurs at 5!
    # Time complexity O(logn-base 5)
    n=int(input())
    ans = 0
    while n > 0:
        n //= 5
        ans += n
    print(ans)