class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        is_valid = True
        
        dictionary = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        if s[0] not in dictionary.keys():
            is_valid = False
        else:
            look_up = []
            
            for bracket in s:
                if bracket in dictionary.keys():
                    look_up.append(bracket)
                else:
                    if len(look_up) != 0:
                        if bracket == dictionary[look_up[-1]]:
                            del look_up[-1]
                        else:
                            is_valid = False
                            break
                    else:
                        is_valid = False
                        
            if len(look_up) != 0:
                is_valid = False
                            
            
        return is_valid
        