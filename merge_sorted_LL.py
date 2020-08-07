import sys

# Day 1 
# 4. Merge Sorted Linked List
#Example:-
#INPUT:-
# 2 sorted linked list
# 1->2->4, 1->3->4
#OUTPUT:-
# Merged Linked List
# 1->1->2->3->4->4

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
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
        return
