class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        
        for i in range(len(s)):
            value = s[len(s) - 1 - i]
            
            if value == ' ' and counter != 0:
                break 
            
            if value != ' ':
                counter += 1
        
        return counter 
    #len(s.strip().split(' ')[-1])