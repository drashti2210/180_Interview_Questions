import sys

# Day 2
# 4. Inversion of Array (Using Merge Sort)
# INPUT:-
# 1st line no of test cases-t
# list of integers
# 1
# 1 20 6 4 5
# OUTPUT: -
# no of counts to be sorted array
# 5

sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

for i in range(int(input())):
    arr=list(map(int,input().split()))
    n=len(arr)
    # solution 1 by brute force
    # Time Complexity O(n^2) Space Complexity O(1)
    count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                count += 1
    print(count)