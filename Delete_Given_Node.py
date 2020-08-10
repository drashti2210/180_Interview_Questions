import sys

# Delete a given Node when a node is given. (O(1) solution
# INPUT:-
# node to be deleted
# linked list:=>> 1->2->3->4->5->NULL
# 2
# OUTPUT: -
# void
# linked list will be:=>> 1->3->4->5->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def delNode(node):

    # solution 1 using loop till node
    # Time Complexity O(n)
    while node.next:
        node.val = node.next.val
        prev = node
        node = node.next
    prev.next = None

    # solution 2
    # Time Complexity O(1) Space Complexity O(1)
    node.val, node.next.val = node.next.val, node.val
    node.next = node.next.next