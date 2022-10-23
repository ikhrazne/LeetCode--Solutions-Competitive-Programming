# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        tree1 = []
        tree2 = []
        
        def preorder_traverse(root, which_tree):
            
            if root is None:
                return 
            
            if which_tree == 'first':
                tree1.append(root.val)
            else:
                tree2.append(root.val)
            
            if root.left is None and root.right is not None:
                if which_tree == 'first':
                    tree1.append(None)
                else:
                    tree2.append(None)
                
            preorder_traverse(root.left, which_tree)
            preorder_traverse(root.right, which_tree)
            
        
        preorder_traverse(p, 'first')
        preorder_traverse(q, 'second')
        
        return tree1 == tree2
            
        