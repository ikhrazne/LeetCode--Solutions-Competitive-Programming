class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        second_number = ''.join([str(x)[i] for i in range(len(str(x)) - 1, -1, -1)])
        
        return str(x) == second_number