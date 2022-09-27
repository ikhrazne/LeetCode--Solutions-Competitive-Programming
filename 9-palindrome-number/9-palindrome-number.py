class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        reverse_x = ''.join([str(x)[i] for i in range(len(str(x)) - 1, -1, -1)])
        
        return str(x) == reverse_x