import sys

#Day 5
# 6. Add two numbers as LinkedList
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

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    # sotion 1
    # using another linked list to store sum
    dummy = cur = ListNode(-1)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry%10)
        cur = cur.next
        carry //= 10
    return dummy.next

    # solution 2
    # recursive approach
    temp = l1.val + l2.val
    digit, tenth = temp% 10, temp// 10
    answer = ListNode(digit)
    if any((l1.next, l2.next, tenth)):
        if l1.next:
            l1 = l1.next 
        else: 
            l1 = ListNode(0)
        if l2.next:
            l2 = l2.next 
        else:
            l2=ListNode(0)
        l1.val += tenth
        answer.next = self.addTwoNumbers(l1, l2)    
    return answer