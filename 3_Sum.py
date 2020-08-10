import sys
# 3 Sum Problem
# INPUT:-
# size of array,array
# 6
# -1 0 1 2 -1 -4
# OUTPUT: -
# [[-1, -1, 2]
# [-1, 0, 1]]

n=int(input())
arr=list(map(int,input().split()))

# solution 1
# brute force approach - with repeating elements
# using 3 loops
# Time Complexity O(n^3) Space Complexity O(1)
def three_sum(arr,n):
    ans=set()
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    ans.add((arr[i],arr[j],arr[k]))
    return list(ans)

# solution 2
# By extending 2 sum
# Time complexity O(n^2) Space Complexity O(1)
def three_sum(nums,n):
    nums = sorted(nums)
    result = set()
    for i in range(n):
        l = i + 1
        r = len(nums) - 1
        target = 0 - nums[i]
        while l < r:
            if nums[l] + nums[r] == target:
                result.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return list(result)

# solution 3
# another approach by sorting
# Time Complexity O(n) Space Complexity O(1)

def three_sum(nums,n):
    res = []
    nums.sort()
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res
