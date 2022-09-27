class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        characters = {'I': 1,
                      'V': 5,
                      'X': 10,
                      'L': 50,
                      'C': 100,
                      'D': 500,
                      'M': 1000}
        result = 0
        i = 0
        
        while i < len(s):
            if i + 1 >= len(s):
                result += characters[s[i]]
                break
                
            if s[i] == 'I' and s[i + 1] in ['V', 'X']:
                result += characters[s[i + 1]] - 1
                i += 1
            elif s[i] == 'X' and s[i +  1] in ['L', 'C']:
                result += characters[s[i + 1]] - 10
                i += 1
            elif s[i] == 'C' and s[i + 1] in ['D', 'M']:
                result += characters[s[i + 1]] - 100
                i += 1
            else:
                result += characters[s[i]]
            
            i += 1
        
        return result