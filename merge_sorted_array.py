import sys

sys.stdout = open('d:/Coding/output.txt','w')
sys.stdin = open('d:/Coding/input.txt','r')

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Example
# INPUT
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# OUTPUT
# [1,2,2,3,5,6]

nums1=list(map(int,input().split()))
m=int(input())
nums2=list(map(int,input().split()))
n=int(input())

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Solution 1
        # check greater & append in nums1
        if n==0:
            return
        elif m == 0:
            j = 0
            for j in range(n):
                nums1[j] = nums2[j]
        i, j = m-1, n-1
        temp = 0
        while i>=0 and j>=0:
            if nums1[i] >= nums2[j]:
                nums1[m+n-temp-1] = nums1[i]
                i-=1
                temp+=1
            else:
                nums1[m+n-temp-1] = nums2[j]
                j-=1
                temp+=1
        if j < 0:
            return
        else:
            while j>=0:
                nums1[m+n-temp-1]=nums2[j]
                j-=1
                temp+=1
        print(nums1)
        return

        # Solution 2
        # Using Sort
        for i in range(n):
            nums1[i+m] = nums2[i]
        nums1.sort()

merge(nums1,m,nums2,n)

print(nums1)