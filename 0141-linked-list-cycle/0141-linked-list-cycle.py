# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        remember_node = ListNode(0)
        value = None
        while True:
            
            if head is None:
                return False
            
            if head == remember_node:
                return True
            
            value = head.next
            head.next = remember_node
            head = value
            
            
            
            
        