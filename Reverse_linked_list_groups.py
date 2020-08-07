import sys

#Day 6
# 3. Reverse a LinkedList in groups of k
# INPUT:-
# linked list & k
# 1->2->3->4->5->NULL
# 3
# OUTPUT: -
# 3->2->1->4->5->->NULL

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head,k):
    # solution 1
    # iterative approach
    # for each sub-LL of size k reverse that & join with preveous sub-LL
    dummy = jump = ListNode(0)
    dummy.next = l = r = head
    while True:
        count = 0
        while r and count < k:  
            r = r.next
            count += 1
        if count == k:  
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur  
            jump.next, jump, l = pre, l, r  
        else:
            return dummy.next

    # solution 2
    # recursive approach
    
    # Check if we need to reverse the group
    curr = head
    for _ in range(k):
        if not curr: return head
        curr = curr.next		
    # Reverse the group (basic way to reverse linked list)
    prev = None
    curr = head
    for _ in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt	
    # After reverse, we know that `head` is the tail of the group.
	# And `curr` is the next pointer in original linked list order
    head.next = self.reverseKGroup(curr, k)
    return prev