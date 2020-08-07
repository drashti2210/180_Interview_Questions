import sys

#Day 5
# 3. Merge 2 Sorted Linked List
# INPUT:-
# 1->3->6->NULL
# 2->4->7->->NULL
# OUTPUT: -
# 1->2->3->4->6->7->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def mergeTwoLists(l1,l2):
    # solution iterative
    # Traverse throught elements of linked list and copare 
    # then insert these in list
    # after that insert the remaining elements
    head = ListNode(0)
    temp = head     
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next     
    while l1:
        temp.next = l1
        l1 = l1.next
        temp = temp.next
    while l2:
        temp.next = l2
        l2 = l2.next
        temp = temp.next
    head = head.next
    return head

    # solution iterative
    # inplace solution
    if None in (l1, l2):
        return l1 or l2
    dummy = cur = ListNode(0)
    dummy.next = l1
    while l1 and l2:
        if l1.val < l2.val:
            l1 = l1.next
        else:
            nxt = cur.next
            cur.next = l2
            tmp = l2.next
            l2.next = nxt
            l2 = tmp
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

    # solution recursive
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2