import sys

#Day 5
# 4. Remove N-th node from back of LinkedList
# INPUT:-
# Linked list & n
# 1->2->3->4->5->NULL
# 2
# OUTPUT: -
# 1->2->3->5->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    # solution 1
    # using length of linked list
    temp = head
    i = 0
    while temp:
        temp = temp.next
        i += 1
    temp = head
    step = i-n
    if step == 0:
        head = head.next
    else:
        l = 1
        while l<step :
            temp = temp.next
            l += 1
        temp.next = temp.next.next
    return head

    # solution 2
    # using fast and slow pointer
    fast = slow = head
    for i in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
