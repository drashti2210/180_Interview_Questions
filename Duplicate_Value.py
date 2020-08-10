import sys
import collections

# Find the duplicate in an array of N+1 integers. 
# Example
# INPUT:-
# 1st line no. of test cases-t
# next t lines input for each test cases
    #array of size n+1
# 3
# 1 3 2 5 4 6 7 8 5 9
# 1 1 2 3
# 1 3 4 5 2 5
# OUTPUT:-
# 5
# 1
# 5

for t in range(int(input())):
    lst=list(map(int,input().split()))
    n=len(lst)
    ans=0
    #solution 1 - brute force 
    #Time complexity: O(n^2) Space Complexity: O(1)
    for i in range(n):
        for j in range(i+1,n):
            if lst[i]==lst[j]:
                ans=lst[j]
                break
    print(ans)

    #solution 2 - using counter
    #Time Complexity O(n) Space Complexity O(n)
    dic=collections.Counter(lst)
    for i in dic:
        if dic[i]>1:
            print(i)
    
    #solution 3 - sorting
    #Time Complexity O(nlogn) Space Complexity O(1)

    lst.sort()
    for i in range(n-1):
        if lst[i]==lst[i+1]:
            print(lst[i])
            break

    #solution 4 - using another array
    #Time complexity O(n) Space Complexity O(n)

    arr=[0]*n
    for i in range(n):
        if arr[lst[i]]==1:
            print(lst[i])
            break
        else:
            arr[lst[i]]=1