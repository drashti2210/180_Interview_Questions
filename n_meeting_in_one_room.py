import sys
sys.stdout = open('d:/Coding/output.txt','w')
sys.stdin = open('d:/Coding/input.txt','r')

# Find maximum meetings in one room
# There is one meeting room in a firm. 
# There are N meetings in the form of (S[i], F[i]) 
# where S[i] is the start time of meeting i and F[i] is finish time of meeting i. 
# The task is to find the maximum number of meetings that can be accommodated in the meeting room. 
# Print all meeting numbers

# Example
# INPUT
# 1
# 1 3 0 5 8 5
# 2 4 6 7 9 9
# OUTPUT
# [(1, 2), (3, 4), (5, 7), (8, 9)]

for _ in range(int(input())):
    s=list(map(int,input().split()))
    f=list(map(int,input().split()))
    n=len(s)

    pairs = [(s[i],f[i]) for i in range(n)]
    pairs.sort(key = lambda x : x[1])
    ans=[]
    ans.append(pairs[0])
    temp=pairs[0][1]
    for i in range(1,n):
        if pairs[i][0]>temp:
            temp=pairs[i][1]
            ans.append(pairs[i])
    print(ans)
# Leetcode meeting room
# Given an array of meeting time intervals consisting of start and end times [s1, e1], [s2, e2], ... , determine 
# if a person could attend all meetings.

# For example,
# Given [ [0, 30], [5, 10], [15, 20] ],
# return false.
    pairs.sort(key = lambda x : x[1])
    for i in range(n-1):
        if pairs[i][1]>[i+1][0]:
            print(False)
            break
    print(True)

# Leetcode meeting room 2
# Given an array of meeting time intervals consisting of start and 
# end times [[s1,e1],[s2,e2],...] find the minimum number of conference rooms required.
# For example,
# Given [ [0, 30], [5, 10], [15, 20] ]
# return 2






