# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        
        def preorder_travers(root):
            nodes.append(root.val)
            
            if root.left:
                preorder_travers(root.left)
            
            if root.right:
                preorder_travers(root.right)
        if root:
            preorder_travers(root)
            
        return nodes