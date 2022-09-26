class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results = []
        
        for i, number in enumerate(nums):
            difference = target - number
            
            if difference in nums:
                if nums.index(difference) == i:
                    pass 
                else:
                    results = [i, nums.index(difference)]
                    break
                
        return results
            
            