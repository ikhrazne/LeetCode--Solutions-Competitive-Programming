
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        
        count = 2
        
        while count <= n:
            
            if count == n:
                return True
            
            count *= 2
            
        return False
        
            
            
        