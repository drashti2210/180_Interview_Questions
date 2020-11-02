import sys
sys.stdout = open('d:/Coding/output.txt','w')
sys.stdin = open('d:/Coding/input.txt','r')
# Trapping Rain Water
# INPUT:-
# Array of height of building
# 0 1 0 2 1 0 1 3 2 1 2 1
# OUTPUT:-
# 6


# solution 1
# using 2 poiters
# Time Complexity O(n)

for t in range(int(input())):
        height=list(map(int,input().split()))
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
                
        print(result)

for t in range(int(input())):
        height=list(map(int,input().split()))
