import sys

#Day 5
# 1. Reverse Linked List
# INPUT:-
# 1->2->3->4->5->NULL
# OUTPUT: -
# 5->4->3->2->1->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head):
    # recursive approach
    if head is None or head.next is None:
        return head
    temp=self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return temp

    # iterative approach
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev