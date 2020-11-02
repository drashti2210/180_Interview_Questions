import sys
import collections
sys.stdout = open('d:/Coding/output.txt','w')
sys.stdin = open('d:/Coding/input.txt','r')

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        node = ListNode(0)
        node.next = temp = head
        
        while head and head.next:
            
            if head.val > head.next.val:
                
                temp = head.next
                prev = node
                
                while prev.next.val < temp.val:
                    prev = prev.next
                    
                head.next = temp.next
                temp.next = prev.next
                prev.next = temp
            else:
                head = head.next
            
        return node.next
                