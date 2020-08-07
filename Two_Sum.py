import sys

#Day 4
# 1. 2 sum
# INPUT:-
# array & target
# 1
# 2 7 11 15
# 9
# OUTPUT:-
# indices of sum=target
# 0 1

#input output files
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

for t in range(int(input())):
    arr=list(map(int,input().split()))
    target=int(input())
    n=len(arr)
    # solution 1 brute force approach
    # Time Complexity O(n^2)
    flag=0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j]==target:
                flag=1
                print(i,j)
                break
        if flag==1:
            break

    # solution 2 using hashing
    # Time Comlexity O(n)
    required = {}
    for i in range(n):
        if target - arr[i] in required:
            print(required[target - arr[i]],i)
        else:
            required[arr[i]]=i

                
