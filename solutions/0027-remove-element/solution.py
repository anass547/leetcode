class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n=len(nums)
        nums[:]=filter(lambda a: a != val, nums)
        

        return len(nums)
        
