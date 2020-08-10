import sys

# Inversion of Array (Using Merge Sort)
# INPUT:-
# list of integers
# 1 20 6 4 5
# OUTPUT: -
# no of counts to be sorted array
# 5

arr=list(map(int,input().split()))
n=len(arr)
    
def inversion_array(arr,n):
    # solution 1 by brute force
    # Time Complexity O(n^2) Space Complexity O(1)
    count = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            if (arr[i] > arr[j]): 
                count += 1
    return(count)