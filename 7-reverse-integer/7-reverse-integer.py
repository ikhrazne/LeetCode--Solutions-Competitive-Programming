class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)[::-1]
        
        if x[len(x) - 1] == '-':
            x = '-' + x[:-1]
            
        if x[0] == 0:
            x = x[1:]
            
        return int(x) if int(x) < 2**31 and int(x) > -2 ** 31 else 0 
        