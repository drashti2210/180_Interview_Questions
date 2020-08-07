import sys

#Day 6
# 2. Palindrome Linked List
# INPUT:-
# linked list
# 1->2->3->2->1->NULL
# OUTPUT: -
# True

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(self, head: ListNode) -> bool:
    # solution 1
    # using array/list
    vals = []
    while head:
        vals += head.val,
        head = head.next
    return vals == vals[::-1]

    # solution 2
    # using fast and slow pointers
    # compare reverse of 1st half with 2nd half
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    return not rev