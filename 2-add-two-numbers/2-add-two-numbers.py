# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        results = ListNode()        
        final = results
        c = 0
        compute = 0
        while l1 or l2:
            a = 0
            b = 0 
            if l1 is not None:
                a = l1.val
                l1 = l1.next
            
            if l2 is not None:
                b = l2.val
                l2 = l2.next
            
            compute = a + b + c
            
            if len(str(compute)) > 1:
                c = 1
                final.next = ListNode(int(str(compute)[1]))
            else:
                final.next = ListNode(compute)
                c = 0
            
            if l1 is None and l2 is None and c == 1:
                final = final.next
                final.next = ListNode(c)   
                
            final = final.next
        
        return results.next
        
        
        