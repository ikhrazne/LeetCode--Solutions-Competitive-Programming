class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dictionary = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        
        result = ''
        
        for i, n in enumerate(str(num)):
            help_number = int(n) * 10**(len(str(num)) - 1 - i)
            
            if int(n) in [4, 9]:
                if len(str(num)) - 1 - i == 2:
                    if int(n) == 4:
                        result += 'CD'
                    else:
                        result += 'CM' 
                elif len(str(num)) - 1 - i == 1:
                    if int(n) == 4:
                        result += 'XL'
                    else:
                        result += 'XC'
                else:
                    if int(n) == 4:
                        result += 'IV'
                    else:
                        result += 'IX'
                
            elif int(n) - 5 == 0:
                result += dictionary[help_number]
            elif int(n) - 5 > 0 :
                result += dictionary[5 * 10**(len(str(num)) - 1 - i)]
                rest = int(n) - 5
                for a in range(rest):
                    result += dictionary[10**(len(str(num)) - i - 1)]
            else:
                for a in range(int(n)):
                    result += dictionary[10**(len(str(num)) - i - 1)]
            
        
        return result
            
            
        