class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False
        window = set()

        for i in range(len(nums)):
            if nums[i] in window :
                return True
            
            window.add(nums[i])
            if i >= k:
                window.discard(nums[i-k])
            
            
            
            
        return False

