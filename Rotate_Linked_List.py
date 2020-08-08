import sys

#Day 6
# 6. Rotate Linked List by k
# INPUT:-
# linked list
# 1->2->3->4->5->NULL 2
# OUTPUT: -
# 4->5-> 1->2->3->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def rotateRight(head, k):
    # solution 
    # using length of the linked list
    # Time Complexity O(n)
    if not head:
        return None
    last = head
    length = 1
    while ( last.next ):
        last = last.next
        length += 1
    if k>=length:
        k=k%length    
    last.next = head
    temp = head
    for i in range( length - k - 1 ):
        temp = temp.next
    answer = temp.next
    temp.next = None    
    return answer