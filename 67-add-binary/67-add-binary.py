class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ''
        i = 0
        memory = 0
        
        result = list(str(int(a) + int(b)))
        
        for i in range(len(result) - 1, -1, - 1):
            
            result[i] = str(int(result[i]) + memory)
            memory = 0
            
            if result[i] == '2':
                result[i] = '0'
                memory = 1
            elif result[i] == '3':
                result[i] = '1'
                memory = 1
            else:
                pass 
        
        if memory == 1:
            result = ['1'] + result
            
        
        return ''.join(result)
        