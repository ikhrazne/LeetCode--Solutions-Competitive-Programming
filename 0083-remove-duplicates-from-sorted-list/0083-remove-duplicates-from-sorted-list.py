# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        
        result = ListNode(head.val)
        pointer = result
        remembered_set = set()
        
        while True:
            
            if head is None:
                result.next = None
                return pointer
            
            remembered_set.add(head.val)
            
            head = head.next
            
            if head is None:
                result.next = None
                return pointer
            
            if head.val in remembered_set:
                pass
            else:
                result.next = ListNode(head.val)
                result = result.next