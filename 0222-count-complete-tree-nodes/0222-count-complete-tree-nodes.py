# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        
        def traverse(node):
            value = 0
            if node:
                value += 1
                value += traverse(node.left)
                value += traverse(node.right)
            
            return value 
        
        result = traverse(root)
        
        return result
        