class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:]=list(sorted(set(nums)))

        return len(nums)
        
