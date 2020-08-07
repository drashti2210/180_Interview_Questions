import sys

#Day 4
# 4. Longest subarray with sum 0
# INPUT:-
# array
# 1
# 1 -3 1 0 0 -1 3 0 3 -1 -1 -1
# OUTPUT:-
# 11

#input output files
sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')


for t in range(int(input())):
    arr=list(map(int,input().split()))
    n=len(arr)
    # solution 1 brute force
    # use 2 loops Time Complexity O(n^2)
    max_len = 0
    for i in range(n):
        curr_sum = 0 
        for j in range(i,n): 
            curr_sum += arr[j] 
            if curr_sum == 0: 
                max_len = max(max_len, j-i + 1) 
    print(max_len)

    # solution 2 using hash map
    # Time Complexity O(n) space Complexity O(n)
    hash_map = {}  
    max_len = 0
    curr_sum = 0 
    for i in range(n): 
        curr_sum += arr[i] 
        if arr[i]==0 and max_len==0: 
            max_len = 1
        if curr_sum==0: 
            max_len = i + 1
        if curr_sum in hash_map: 
            max_len = max(max_len, i - hash_map[curr_sum] ) 
        else:  
            hash_map[curr_sum] = i 
  
    print(max_len) 