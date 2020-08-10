import sys

# detect a cycle & remove loop in linked lis
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

def detectloop(head):
    # solution 
    # using fast & slow pointers
    slow=fast=head
    while slow and fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            print('True')
            break
        else:
            print('False')

def removeloop(node):
    ptr1 = self.head 
    while(1): 
        ptr2 = loop_node 
        while(ptr2.next != loop_node and ptr2.next != ptr1): 
            ptr2 = ptr2.next  
        if ptr2.next == ptr1 :  
            break       
        ptr1 = ptr1.next     
    ptr2.next = None