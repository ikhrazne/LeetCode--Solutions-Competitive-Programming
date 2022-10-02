class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        
        word = strs[0]
        
        for i in range(len(word)):
            char = word[i]
            is_true = True
            
            for j in range(1, len(strs)):
                if i >= len(strs[j]):
                    is_true = False
                    break
                    
                if char != strs[j][i]:
                    is_true = False
                    break
                    
            if is_true == True:
                prefix += char
            else:
                break
        
        return prefix 
            
        