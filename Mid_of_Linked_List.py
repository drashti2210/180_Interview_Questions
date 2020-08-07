import sys

#Day 5
# 2. Middle of Linked List
# INPUT:-
# 1->2->3->4->5->NULL
# OUTPUT: -
# 3

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def middleNode(head):
    # solution 1 
    # find the length of linked list
    # iterate upto mid & return mid element
    l=0
    temp=head
    while temp.next!=None:
        temp=temp.next
        l+=1
    if l%2!=0:
        l=(l//2)+1
    else:
        l=l//2
    for i in range(l):
        head=head.next
    return head

    # solution 2
    # using array
    arr = [head]
    while arr[-1].next:
        arr.append(arr[-1].next)
    return A[len(arr) // 2]

    # solution 3
    # using slow & fast poiter
    # When fast reaches the end of the list, slow must be in the middle.
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow