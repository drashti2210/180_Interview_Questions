import sys

# Trapping Rain Water
# INPUT:-
# Array of height of building
# 0 1 0 2 1 0 1 3 2 1 2 1
# OUTPUT:-
# 6

height=list(map(int,input().split()))

# solution 1
# By traversing array till ith index
def maxWater(height): 
    n=len(height)
    res = 0
    for i in range(1, n - 1) :  
        left = arr[i];  
        for j in range(i) : 
            left = max(left, arr[j])
        right = arr[i];  
        for j in range(i + 1 , n) :  
            right = max(right, arr[j])
        res = res + (min(left, right) - arr[i])
    return res;  

# solution 2
# using 2 poiters
# Time Complexity O(n)
def trap(height):
        result = 0
        i = 0
        j = len(height) - 1
        lmax = rmax = 0
        while (i <= j):
            lmax = max(lmax, height[i])
            rmax = max(rmax, height[j])
            if lmax <= rmax:
                result += lmax -  height[i]
                i+=1
            elif rmax <= lmax:
                result += rmax - height[j]
                j-=1
                
        return result