import sys

#Day 6
# 1. Find intersection point of linked list
# INPUT:-
# 2 linked list
# 1->2->3->->NULL
# 1->2->3->->NULL
# OUTPUT: -
# addition
# 2->4->6->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

    # solution 1 brute force
    # using 2 loop
    curr1=headA
    while curr1:
        curr2=headB
        while curr2:
            if curr1==curr2:
                return curr1
            else:
                curr2=curr2.next
        curr1=curr1.next

    # solution 2 
    # by iteratingg through both linked list
    curr1,curr2=headA,headB
    while curr1!=curr2:
        if curr1==None:
            curr1=headB
        else:
            curr1=curr1.next
        if curr2==None:
            curr2=headA
        else:
            curr2=curr2.next
    return curr1

    # solution 3
    # using length difference 
    curA,curB = headA,headB
    lenA,lenB = 0,0
    while curA is not None:
        lenA += 1
        curA = curA.next
    while curB is not None:
        lenB += 1
        curB = curB.next
    curA,curB = headA,headB
    if lenA > lenB:
        for i in range(lenA-lenB):
            curA = curA.next
    elif lenB > lenA:
        for i in range(lenB-lenA):
            curB = curB.next
    while curB != curA:
        curB = curB.next
        curA = curA.next
    return curA