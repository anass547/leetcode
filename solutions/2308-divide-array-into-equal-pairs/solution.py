class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)%2!=0:
            return False
        for i in range(1,len(nums)):
            if nums.count(nums[i])%2!=0:
                return False
        return True
        
