import sys

# Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that each element 
# appears only once and returns the new length.

# For more clarification of question:
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

sys.stdout = open('d:/Coding/output.txt','w')
sys.stdin = open('d:/Coding/input.txt','r')
nums=list(map(int,input().split()))

# Solution
# 2 pointers 
def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        j=0
        for i in range(1,n):
            if nums[j]!=nums[i]:
                j+=1
                nums[j]=nums[i]
                
        return j+1

