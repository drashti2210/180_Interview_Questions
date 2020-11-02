import sys

# Day 2
# 3. Next Permutation
# INPUT:-
# 1st line no of test cases-t
# list of integers
#1
# 1 2 3
# OUTPUT: -
# Print next permutation
# 1 3 2

sys.stdout = open('d:/Coding/output.txt','w')
sys.stdin = open('d:/Coding/input.txt','r')
for t in range(int(input())):
    # solution by looping
    # inplace solution
    nums=list(map(int,input().split()))
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:   
        nums.reverse()
        break 
    k = i - 1    
    while nums[j] <= nums[k]:
        j -= 1
    nums[k], nums[j] = nums[j], nums[k]  
    l, r = k+1, len(nums)-1  
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l +=1 
        r -= 1
    print(nums)