import sys
#Day-1
#5. Kadane's Algorithm
#Example
#Input: -
# 1st line no. of test cases-t
# next t lines input for each test cases
    #1st line size of array (n)
    #elements of array of size n
# Example
# 2
# 3
# 3 2 -1
# 6
# -1 3 4 -5 2 6
#OUTPUT:-
#Largest sum countiguous sub array
# 5
# 10

sys.stdout = open('d:/Coding/30daysSDE/output.txt','w')
sys.stdin = open('d:/Coding/30daysSDE/input.txt','r')

#Largest sum countiguous sub array
#Time Complexity O(n)
for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    maxm = 0
    maximum = 0
    for i in range(0, n): 
        maximum = maximum + arr[i] 
        if maximum < 0: 
            maximum = 0
        elif (maxm < maximum): 
            maxm = maximum
    print(maxm) 